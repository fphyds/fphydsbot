import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="fhydsbot",
    version="0.0.1",
    author="Zavyalov1",
    author_email="fedruch@gmail.com",
    description="X5School project fhydsbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Zavyalov1/fphydsbot.git",
    packages=setuptools.find_packages(include=['fphydsbot', 'fphydsbot.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "imutils==0.5.2",
        "numpy==1.20.1",
        "opencv-python==4.5.1.48",
        "dlib==19.17.0",
        "PyTelegramBotAPI==3.7.6"],
    python_requires='>=3.8',
)
