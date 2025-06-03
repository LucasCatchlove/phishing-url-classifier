import re

def split_url_into_sections(url: str) -> list[str]:
    domain = extract_domain(url)
    directory =extract_directory(url)
    filename = extract_filename(url)
    parameters = extract_parameters(url)
    return (domain, directory, filename, parameters)

def extract_domain(url: str) -> str:
    pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return ""

def extract_directory(url: str) -> str:
    pattern = r'(?:https?://)?(?:www\.)?[^/]+(/[^?]*)?'
    match = re.search(pattern, url)
    if match:
        return match.group(1) if match.group(1) else "/"
    return ""

def extract_filename(url: str) -> str:
    pattern = r'(?:https?://)?(?:www\.)?[^/]+(?:/([^/?]+))?'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return ""

def extract_parameters(url: str) -> str:
    pattern = r'\?([^#]*)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return ""
        