from typing import NewType
import uuid


class UrlToClassify:
  
    def __init__(self, url: str):
        self.url = url
        
        if not isinstance(url, str):
            raise ValueError("url is not a string")
        elif len(url.strip()) == 0:
            raise ValueError("url is an empty string")
        else:
            self.url = url
            

        
