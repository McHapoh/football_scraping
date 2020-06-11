import re
import requests
import pandas as pd
import os
from bs4 import BeautifulSoup, SoupStrainer


def get_data(urls):
    """
    Extract data from a set of HTML pages, and convert them into a .csv file.

    Args:
        urls ([list]): [List containing all URLs]

    Yields:
        listes_joueurs[csv]: [CSV file containg informations about players]
    """

    only_player_search = SoupStrainer(id="player-search")
    season = ""
    name = ""
    position = ""
    club = ""
    country = ""
    running_index = 2000

    def clean_fmt(soup, token):
        raw = str(soup.select(token))
        raw = re.sub(r"(<.*?>)*?", '', raw)

        raw = raw.replace("  ", "").replace("\r", "").replace(
            "\n", "").replace("[", "").replace("]", "").lstrip().rstrip().lstrip().rstrip()
        return raw

    def gen_url_index():
        for i in range(0, len(urls)):
            yield urls[i]

    gen = gen_url_index()

    for gui in gen:
        url = open(f"{gui}.html", encoding="utf8")
        soup = BeautifulSoup(url, "lxml", parse_only=only_player_search)

        name_token = "div.player-search-row-player"
        position_token = "div.player-search-row-position.desktop-item"
        club_token = "div.player-search-row-club.desktop-item"
        country_token = "div.player-search-row-country.desktop-item"

        name_int = clean_fmt(soup, name_token)
        name += name_int + ", "
        count = len(list(name_int.split(", ")))
        while count > 0:
            season += f"{running_index}, "
            count -= 1

        position += clean_fmt(soup, position_token) + ", "
        club += clean_fmt(soup, club_token) + ", "
        country += clean_fmt(soup, country_token) + ", "

        clean_name = list(name.split(", "))
        clean_season = list(season.split(", "))
        clean_position = list(position.split(", "))
        clean_club = list(club.split(", "))
        clean_country = list(country.split(", "))

        s1 = pd.Series(clean_season, name='season')
        s2 = pd.Series(clean_name, name='name')
        s3 = pd.Series(clean_position, name='position')
        s4 = pd.Series(clean_club, name='club')
        s5 = pd.Series(clean_country, name='country')

        df = pd.concat([s1, s2, s3, s4, s5], axis=1)

        if os.path.exists(os.path.join("csv/LIGUE1/sources")):
            df.to_csv(fr'csv/LIGUE1/sources/liste_joueurs_{running_index}.csv')
        else: 
            os.makedirs(os.path.join("csv/LIGUE1/sources"))
            df.to_csv(fr'csv/LIGUE1/sources/liste_joueurs_{running_index}.csv')
        running_index += 1
