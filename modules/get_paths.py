def get_paths(link, nb):
    """
    Generate a list containing all URLs

    Args:
        link [str]: Base HTML link 
        nb [int]: Number of pages usingHTML link

    Returns:
        url [str]: [List containing all URLs]
    """

    url = []

    for si in range(2000, 2020):
        for ti in range(1, nb+1):
            result = link + str(si) + "-" + str(si+1) + "&teamId=" + str(ti)
            url.append(result)
    return url
