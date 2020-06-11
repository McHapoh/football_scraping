from urllib import request
import os

def download_urls(urls, token):
    """
    Function to download web pages in html format.

    Args : 
        urls [list] : List of urls you want to download.
    """
    for i in urls:
        name = i[31+len(token):]
        if os.path.exists(os.path.join("html/WFDB")):
            request.urlretrieve(i, fr'html/WFDB/{name}_{token}.html')
        else:
            os.makedirs(os.path.join("html/WFDB"))
            request.urlretrieve(i, fr'html/WFDB/{name}_{token}.html')
