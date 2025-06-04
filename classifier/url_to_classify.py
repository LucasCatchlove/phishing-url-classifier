import numpy as np
import pandas as pd
from measured_features import MeasuredFeatures
from url_structure_features import get_structural_features
from static_data import FEATURE_LIST
from phishing_url_classifier import phishing_url_classifier

class UrlToClassify:
      
    def __init__(self, url: str):
        self.url: str = url
        self.prediction: bool | None = None
        self.features: None | dict[str, any] = dict.fromkeys(FEATURE_LIST)
        
        if not isinstance(url, str):
            raise TypeError(f"url is not a string (url provided is of type {type(url).__name__})")
        
        if len(url.strip()) == 0:
            raise ValueError("url is an empty string")
        
        self.url = url
            
    def build_features(self) -> dict[str, any]:
        measured_features = MeasuredFeatures(self.url).get_measured_features()
        structural_features = get_structural_features(self.url)
        features = measured_features | structural_features
        
        #to preserve ordering
        for feature_label in FEATURE_LIST:
            self.features[feature_label] = features[feature_label]
        
        return self.features
            
    def get_features(self):
        return self.build_features()

    def is_phishing(self):
        sample = self.get_features()
        df = pd.DataFrame([sample])
        return phishing_url_classifier.predict(df)

        
