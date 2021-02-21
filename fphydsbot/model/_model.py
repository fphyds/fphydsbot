import numpy as np
import imutils
import cv2
import os


class Model:
    """
    A class to represent a model for detection faces, predicting genders and ages by photo

    Attributes
    ----------
    model_mean_values : list
        list of model's mean values

    age_list : list
        list of ages predicted by the model

    gender_list : list
        list of genders predicted by the model

    net : Net
        net for detection faces

    age_net : Net
        net for predicting ages

    gender_net : Net
        net for predicting genders

    Methods
    -------
    predict(image) :
        predict detected faces, genders and ages by given image
    """
    def __init__(self):
        path = f'{os.path.dirname(os.path.abspath(__file__))}/models'

        with open(f"{path}/model_weights.txt", 'r') as f:
            self.model_mean_values = [float(value) for value in f.readlines()]

        self.age_list = [
            '(0, 2)',
            '(4, 6)',
            '(8, 12)',
            '(15, 20)',
            '(25, 32)',
            '(38, 43)',
            '(48, 53)',
            '(60, 100)'
        ]

        self.gender_list = ['Male', 'Female']

        self.net = cv2.dnn.readNetFromCaffe(
            f"{path}/deploy.prototxt",
            f"{path}/res10_300x300_ssd_iter_140000.caffemodel"
        )

        self.age_net = cv2.dnn.readNetFromCaffe(
            f"{path}/deploy_age.prototxt",
            f"{path}/age_net.caffemodel"
        )

        self.gender_net = cv2.dnn.readNetFromCaffe(
            f"{path}/deploy_gender.prototxt",
            f"{path}/gender_net.caffemodel"
        )

    def predict(self, image):
        # Resize image
        image, dst_width, dst_height, factor = resize(image)

        # Detect faces
        det_input = image.transpose(2, 0, 1)
        det_input = det_input.reshape(1, *det_input.shape)
        self.net.setInput(det_input)
        frames = self.net.forward()
        frames = frames.reshape(*frames.shape[2:])[:, 2:]

        boxes = []
        genders = []
        ages = []

        for frame in frames:
            if frame[0] < 0.9:
                continue
            else:
                frame = frame[1:]

            # Create boxes
            x1, y1, x2, y2 = frame_coordinates(frame, dst_width, dst_height)
            boxes.append(np.array([x1, y1, x2, y2]) * factor)
            face_image = image[y1:y2, x1:x2].copy()
            blob2 = cv2.dnn.blobFromImage(face_image, 1, (227, 227), self.model_mean_values, swapRB=False)

            # Predict gender
            self.gender_net.setInput(blob2)
            predicted_gender = self.gender_net.forward()
            gender = self.gender_list[predicted_gender[0].argmax()]
            genders.append(gender)
            
            # Predict age
            self.age_net.setInput(blob2)
            predicted_age = self.age_net.forward()
            age = self.age_list[predicted_age[0].argmax()]
            ages.append(age)

        return boxes, genders, ages


def frame_coordinates(frame, dst_width, dst_height, a=0.1):
    """
    A function to transform coordinates of given frame
    by factors dst_width and dst_height and extending parameter a

    :param frame:
    :param dst_width:
    :param dst_height:
    :param a:
    :return:
    """
    x1, y1, x2, y2 = frame
    x1, y1, x2, y2 = int(x1 * dst_width), int(y1 * dst_height), int(x2 * dst_width), int(y2 * dst_height)

    x_dif = x2 - x1
    y_dif = y2 - y1
    x1, x2, y1, y2 = int(x1 - a * x_dif), int(x2 + a * x_dif), int(y1 - a * y_dif), int(y2 + a * y_dif)

    return x1, y1, x2, y2


def resize(image, dst_width=300):
    """
    A function to resize given image by factor dst_width

    :param image:
    :param dst_width:
    :return:
    """
    height, width = image.shape[:2]
    image = imutils.resize(image, width=dst_width)
    factor = width / dst_width
    dst_height = height / factor

    return image, dst_width, dst_height, factor


def transform(image, boxes, genders, ages):
    """
    A function to put detected boxes, genders and ages at image

    :param image:
    :param boxes:
    :param genders:
    :param ages:
    :return:
    """
    image = image.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2

    for box, gender, age in zip(boxes, genders, ages):
        x1, y1, x2, y2 = box.astype(int)
        font_scale = 0.75
        text = "{}, {}".format(gender, age)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Choose best font_scale and get text size for building box around text
        text_width, text_height = cv2.getTextSize(text, font, font_scale, thickness)[0]
        if max(text_width, text_height) > 2 * max(x2 - x1, y2 - y1):
            font_scale /= 1.75
            thickness = 1
            text_width, text_height = cv2.getTextSize(text, font, font_scale, thickness)[0]

        box_coordinates = (int(x1 * 0.999), y1), (x1 + int(text_width * 1.2), y1 - int(text_height * 2.4))
        text_coordinates = (x1 + int(text_width * 0.1), y1 - int(text_height * 0.8))

        cv2.rectangle(image, *box_coordinates, (0, 255, 0), cv2.FILLED)
        cv2.putText(image, text, text_coordinates, font, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

    return image
