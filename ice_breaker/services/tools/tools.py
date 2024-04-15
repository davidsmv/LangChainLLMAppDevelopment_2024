from googlesearch import search

def get_profile_url(text: str) -> str:
    """Searches for Linkedin or Twitter Profile Page

    Args:
        text (str): name of the person and
        aditional descriptions if neccesary

    Returns:
        str: URL
    """
    first_result = next(search(text, num_results=1), None)
    return first_result