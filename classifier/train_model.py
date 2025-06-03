import datetime
import joblib
from sklearn.model_selection import train_test_split
import sklearn.ensemble
import pandas as pd

dataset_raw = pd.read_csv('classifier/data/dataset_full.csv')

y = dataset_raw['phishing']

X = subset = pd.concat([
    dataset_raw.iloc[:, :4],
    dataset_raw.iloc[:, 16:21],    
    dataset_raw.iloc[:, 36:38],  
    dataset_raw.iloc[:, 40:76],
    dataset_raw.iloc[:, 97:108]
], axis=1)

feature_names = list(subset.columns.values)
num_features = len(feature_names)

def train_model(X, y, print_results=False):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    X_train, X_vali, y_train, y_vali = train_test_split(X_train, y_train, test_size=0.2)

    forest = sklearn.ensemble.RandomForestClassifier(random_state=0).fit(X_train, y_train)

    y_pred = forest.predict(X_train)

    training_accuracy = sklearn.metrics.accuracy_score(y_train, y_pred)

    y_pred = forest.predict(X_test)

    test_accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
    
    formatted_results = (
    '{:.2%} training accuracy'.format(training_accuracy),
    '{:.2%} training error'.format(1 - training_accuracy),
    '{:.2%} test accuracy'.format(test_accuracy),
    '{:.2%} test error'.format(1 - test_accuracy),
)
    
    if print_results is True:
        print('{:.2%} training accuracy'.format(training_accuracy))
        print('{:.2%} training error'.format(1-training_accuracy))
        print('{:.2%} test accuracy'.format(test_accuracy))
        print('{:.2%} test error'.format(1-test_accuracy))
    
    joblib.dump(forest, 'classifier/models/model_v1.pkl')
        
    return (forest, formatted_results)

train_model(X, y, print_results=True)




