from modules.get_urls import get_urls
from modules.download_urls import download_urls

from modules.get_paths import get_paths
from modules.get_data import get_data

import os
from glob import glob
import pandas as pd
from unidecode import unidecode

# Download HTML data
url = "https://www.ligue1.fr/listejoueurs?seasonId="
urls = get_urls(url, 100)
download_urls(urls)

# Extract and format data (1 file per season)
path = "html/LIGUE1/seasonId="
paths = get_paths(path, 100)
get_data(paths)

# Append all csv files in one file
extension = "csv"
fichiers = glob(os.path.join(fr"csv/LIGUE1/sources", "*"))
combined_csv = pd.concat([pd.read_csv(f) for f in fichiers ])

if os.path.exists(os.path.join("csv/LIGUE1")):
    combined_csv.to_csv( fr"csv/LIGUE1/liste_joueurs.csv", index=False, encoding='utf-8-sig')
else: 
    os.makedirs(os.path.join("csv/LIGUE1"))
    combined_csv.to_csv( fr"csv/LIGUE1/liste_joueurs.csv", index=False, encoding='utf-8-sig')
