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
