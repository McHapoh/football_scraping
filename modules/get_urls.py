def get_urls(link, nb):
    """
    Generate a list containing all URLs

    Args:
        link [str]: Base HTML link 
        nb [int]: Number of pages usingHTML link

    Returns:
        url [str]: [List containing all URLs]
    """

    def gen_season_index():
        for i in range(2000, 2020):
            yield i

    url = []
    gen = gen_season_index()
    for gsi in gen:
        for i in range(1, nb+1):
            j = link + str(gsi) + "-" + str(gsi+1) + "&teamId=" + str(i)
            url.append(j)
    return url
