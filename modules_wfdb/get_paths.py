def get_paths(link, token):
    """
    Generate a list containing all URLs

    Args:
        link [str]: Base HTML link 

    Returns:
        url [str]: [List containing all URLs]
    """

    url = []
    for i in range(2000, 2020):
        result = link + str(i) + "-" + str(i+1) + f"_{token}"
        url.append(result)
    return url
