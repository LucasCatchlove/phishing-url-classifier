import joblib

_model = None

def init():
    _model = joblib.load('classifier/models/random_forest_classifier.pkl')

