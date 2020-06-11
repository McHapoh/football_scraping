import os
from glob import glob
import pandas as pd

from unidecode import unidecode

from modules_wfdb.get_urls import get_urls
from modules_wfdb.download_urls import download_urls
from modules_wfdb.get_paths import get_paths
from modules_wfdb.get_data import get_data


ref = {
    "goalgetter": "buts_penalty",
    "scorer": "buts_pd"
}

for token, name in ref.items():

    # # Download HTML data
    url = fr"https://www.worldfootball.net/{token}/fra-ligue-1-"
    urls = get_urls(url)
    download_urls(urls, token)

    # # Extract and format data (1 file per season)
    path = "html/WFDB/fra-ligue-1-"
    paths = get_paths(path, token)

    get_data(paths, token, name)

    # Append all csv files in one file
    extension = "csv"
    fichiers = glob(os.path.join(fr"csv/WFDB/sources/{token}", "*"))
    combined_csv = pd.concat([pd.read_csv(f) for f in fichiers])

    if os.path.exists(os.path.join("csv/WFDB")):
        combined_csv.to_csv(
            fr"csv/WFDB/stats_{name}.csv", index=False, encoding='utf-8-sig')
    else:
        os.makedirs(os.path.join("csv/WFDB"))
        combined_csv.to_csv(
            fr"csv/WFDB/stats_{name}.csv", index=False, encoding='utf-8-sig')