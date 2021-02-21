import telebot
import cv2
import os
from fphydsbot.model import Model, transform


class Bot:
    """
    A class to represent a bot interface

    Attributes
    ----------
    bot : Telebot(token)
        instance of Telebot object with certain TOKEN

    Methods
    -------
    run :
        runs the bot in dynamic mode
    """
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def run(self):

        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            text = "Hi! I'm @fphydsbot, I can detect faces, determine human's genders and ages by photo.\n\n"
            text += 'Send me the first photo!\n\n'
            text += 'Source code: '
            self.bot.send_message(message.chat.id, text)

        @self.bot.message_handler(content_types=['photo'])
        def send_photo(message):
            file_id = message.photo[-1].file_id
            file_info = self.bot.get_file(file_id)
            downloaded_file = self.bot.download_file(file_info.file_path)

            path = os.path.dirname(os.path.abspath(__file__))
            with open(f"{path}/photos/{message.chat.id}.jpg", 'wb') as photo:
                photo.write(downloaded_file)

            image_name = f"{path}/photos/{message.chat.id}.jpg"
            out_image_name = f"{path}/out_photos/{message.chat.id}.jpg"

            model = Model()
            image = cv2.imread(image_name)
            boxes, genders, ages = model.predict(image)
            image = transform(image, boxes, genders, ages)
            cv2.imwrite(out_image_name, image)

            out_photo = open(out_image_name, 'rb')
            self.bot.send_photo(message.chat.id, out_photo)

        self.bot.polling()
