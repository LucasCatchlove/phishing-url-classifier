
class UrlToClassify:
      
    def __init__(self, url: str):
        self.url: str = url
        self.prediction: bool | None = None
        self.features = None
        
        if not isinstance(url, str):
            raise TypeError(f"url is not a string (url provided is of type {type(url).__name__})")
        if len(url.strip()) == 0:
            raise ValueError("url is an empty string")
        self.url = url
            

    def get_features(self):
        pass
        
    
    def is_phishing(self):
        if self.prediction is None: 
            raise ValueError("no prediction has been made")
        
        return self.prediction
        
