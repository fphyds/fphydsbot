import setuptools
from fphydsbot.model import download_files


with open("README.md", "r") as fh:
    long_description = fh.read()

download_files(
    urls=[
        'https://www.dropbox.com/s/n2ht3cg23rsw0u0/age_net.caffemodel?dl=1',
        'https://www.dropbox.com/s/yileqhir7e78ivp/deploy_age.prototxt?dl=1',
        'https://www.dropbox.com/s/8d6gru75492ev6p/deploy_gender.prototxt?dl=1',
        'https://www.dropbox.com/s/lhydozqrg9fh7re/deploy.prototxt?dl=1',
        'https://www.dropbox.com/s/dhnkl7fiv0l9zba/gender_net.caffemodel?dl=1',
        'https://www.dropbox.com/s/kr46qohm303yu2y/model_CNN_V2.h5?dl=1',
        'https://www.dropbox.com/s/13ho9xehl3ocfcx/res10_300x300_ssd_iter_140000.caffemodel?dl=1',
        'https://www.dropbox.com/s/ctcyyvudx1s87sn/model_weights.txt?dl=1'
          ],
    file_names=[
        'age_net.caffemodel',
        'deploy_age.prototxt',
        'deploy_gender.prototxt',
        'deploy.prototxt',
        'gender_net.caffemodel',
        'model_CNN_V2.h5',
        'res10_300x300_ssd_iter_140000.caffemodel',
        'model_weights'
    ]
)

setuptools.setup(
    name="distance",
    version="0.0.1",
    author="sggpls",
    author_email="sggplz@yandex.ru",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/saygogoplz/distance.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["textdistance==4.2.0", "Deprecated==1.2.11"],
    python_requires='>=3.8',
)
