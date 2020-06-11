from urllib import request
import os

def download_urls(urls):
    """
    Function to download web pages in html format.

    Args : 
        urls [list] : List of urls you want to download.
    """
    for i in urls:
        name = i[35:]
        if os.path.exists(os.path.join("html/LIGUE1")):
            request.urlretrieve(i, fr'html/LIGUE1/{name}.html')
        else:
            os.makedirs(os.path.join("html/LIGUE1"))
            request.urlretrieve(i, fr'html/LIGUE1/{name}.html')
