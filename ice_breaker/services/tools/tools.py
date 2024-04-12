from googlesearch import search

def get_linkedin_profile_url(text: str) -> str:
    """Searches for LinkedIn Profile POage

    Args:
        text (str): name of the person

    Returns:
        str: URL
    """
    first_result = next(search(text, num_results=1), None)
    return first_result