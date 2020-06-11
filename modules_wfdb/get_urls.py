def get_urls(link):
    """
    Generate a list containing all URLs

    Args:
        link [str]: Base HTML link 
        nb [int]: Number of pages usingHTML link

    Returns:
        url [str]: [List containing all URLs]
    """

    url = []
    for i in range(2000,2020):
        j = link + str(i) + "-" + str(i+1)
        url.append(j)
    return url
