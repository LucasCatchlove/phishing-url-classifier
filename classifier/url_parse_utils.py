import re

from urllib.parse import urlparse, unquote
import os

def extract_domain(url):
    """Extract domain from URL as string"""
    try:
        parsed = urlparse(url)
        return parsed.netloc.split(':')[0] if parsed.netloc else ''
    except:
        return ''

def extract_directory(url):
    """Extract directory path from URL as string"""
    try:
        parsed = urlparse(url)
        if not parsed.path:
            return ''
        path = unquote(parsed.path)
        directory = os.path.dirname(path)
        return directory if directory != '/' else ''
    except:
        return ''

def extract_filename(url):
    """Extract filename from URL as string (only if it has an extension)"""
    try:
        parsed = urlparse(url)
        if not parsed.path:
            return ''
        path = unquote(parsed.path)
        basename = os.path.basename(path)
        # Only return if it has an extension (contains a dot)
        return basename if basename and '.' in basename else ''
    except:
        return ''

def extract_parameters(url):
    """Extract parameters from URL as query string"""
    try:
        parsed = urlparse(url)
        return parsed.query if parsed.query else ''
    except:
        return ''

def split_url_into_sections(url: str) -> list[str]:
    domain = extract_domain(url)
    directory =extract_directory(url)
    filename = extract_filename(url)
    parameters = extract_parameters(url)
    return (domain, directory, filename, parameters)

# def extract_domain(url: str) -> str:
#     pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1)
#     return ""

# def extract_directory(url: str) -> str:
#     pattern = r'(?:https?://)?(?:www\.)?[^/]+(/[^?]*)?'
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1) if match.group(1) else "/"
#     return ""

# def extract_filename(url: str) -> str:
#     pattern = r'(?:https?://)?(?:www\.)?[^/]+(?:/([^/?]+))?'
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1)
#     return ""

# def extract_parameters(url: str) -> str:
#     pattern = r'\?([^#]*)'
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1)
#     return ""
        