import re 

urls = [
    "https://www.example.com/path/to/index.php",
    "http://example.com/index.php",
    "https://subdomain.example.com/path/to/page/index.php?query=1",
    "www.example.org/some/directory/index.html",
    "example.net/image.jpg"
]



def split_url_sections(url):
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

for url in urls: 
    print(split_url_sections(url))