import re

def split_url_into_sections(url):
    domain = extract_domain(url)
    directory =extract_directory(url)
    filename = extract_filename(url)
    parameters = extract_parameters(url)
    return (domain, directory, filename, parameters)

def extract_domain(url):
    pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def extract_directory(url):
    pattern = r'(?:https?://)?(?:www\.)?[^/]+(/[^?]*)?'
    match = re.search(pattern, url)
    if match:
        return match.group(1) if match.group(1) else "/"
    return None

def extract_filename(url):
    pattern = r'(?:https?://)?(?:www\.)?[^/]+(?:/([^/?]+))?'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def extract_parameters(url):
    pattern = r'\?([^#]*)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None
        