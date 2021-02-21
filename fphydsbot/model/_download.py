def download_files(urls, file_names):
    """
    A function for downloading models by urls
    and storing them to files <./models/[file_name]>

    :param urls:
    :param file_names:
    :return:
    """
    import urllib.request
    import ssl
    import os

    for url, file_name in zip(urls, file_names):
        ssl._create_default_https_context = ssl._create_unverified_context
        u = urllib.request.urlopen(url)
        data = u.read()
        u.close()

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, f'models/{file_name}')
        with open(path, "wb") as f:
            f.write(data)


def download():
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
            'model_weights.txt'
        ]
    )
