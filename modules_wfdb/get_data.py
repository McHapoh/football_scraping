import re
import requests
import pandas as pd
import os

from unidecode import unidecode
from bs4 import BeautifulSoup, SoupStrainer


def get_data(urls, token, name):
    """
    Extract data from a set of HTML pages, and convert them into a .csv file.

    Args:
        urls ([list]): [List containing all URLs]

    Yields:
        listes_joueurs[csv]: [CSV file containg informations about players]
    """

    only_player_search = SoupStrainer(id="site")

    def clean_fmt(soup):
        forms = soup.findAll('form')
        for match in forms:
            match.decompose()

        raw = str(soup.select("div.data"))
        raw = re.sub(r"(<.*?>)*?", '', raw)
        raw = raw.replace("(Penalty)","").replace("(", f"\n\n\ndddddd").replace(")","")
        raw_list = list(raw.split("\n\n\n"))

        int_list = []
        for r in raw_list:
            r = re.sub(r'\n', "", r)
            r = unidecode(r)
            int_list.append(r)

        clean_list = []
        for i in range(0, len(int_list)):
            if len(int_list[i]) < 3:
                pass
            else:
                clean_list.append(int_list[i])


        clean_list.pop(0)
        clean_list = [l.replace("Olympique Lyon", "OL").replace("Girondins Bordeaux","FCGB").replace("SC Bastia", "SCB")\
            .replace("Paris Saint-Germain","PSG").replace("Toulouse FC", "TFC").replace("FC Metz", "FCM").replace("AS Saint-Etienne","SE")\
            .replace("EA Guingamp", "EAG").replace("AS Monaco", "ASM").replace("ESTAC Troyes","ESTAC").replace("FC Nantes", "FCN")\
            .replace("AJ Auxerre","AJA").replace("CS Sedan","CSS").replace("Stade Rennes", "SRFC").replace("Olympique Marseille", "OM")\
            .replace("RC Lens", "RCL").replace("RC Strasbourg", "RCS").replace("Lille OSC", "LOSC").replace("Montpellier HSC", "MHSC")\
            .replace("FC Sochaux", "FCSM").replace("FC Lorient", "FCL").replace("Le Havre AC", "HAC").replace("dddddd","") for l in clean_list]

        clean_name = []
        clean_country = []
        clean_club = []
        clean_goal = []

        for i in range(0, int((len(clean_list)/4))):
            clean_name.append(clean_list[i*4])
            clean_country.append(clean_list[1+(i*4)])
            clean_club.append(clean_list[2+(i*4)])
            clean_goal.append(clean_list[3+(i*4)])

        s1 = pd.Series(clean_name, name='name')
        s2 = pd.Series(clean_country, name='country')
        s3 = pd.Series(clean_club, name='goal')
        s4 = pd.Series(clean_goal, name='other')

        df = pd.concat([s1, s2, s3, s4], axis=1)

        return df

    def gen_url_index():
        for i in range(0, len(urls)):
            yield urls[i]

    gen = gen_url_index()

    running_index = 2000
    for gui in gen:
        url = open(f"{gui}.html", encoding="utf8")
        soup = BeautifulSoup(url, "lxml", parse_only=only_player_search)
        df = clean_fmt(soup)
        if os.path.exists(os.path.join(fr"csv/WFDB/sources/{token}")):
            df.to_csv(fr'csv/WFDB/sources/{token}/stats_{name}_{running_index}.csv')
            running_index += 1
        else: 
            os.makedirs(os.path.join(fr"csv/WFDB/sources/{token}"))
            df.to_csv(fr'csv/WFDB/sources/{token}/stats_{name}_{running_index}.csv')
            running_index += 1
