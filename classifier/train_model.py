from sklearn.model_selection import train_test_split
import sklearn.ensemble
import pandas as pd


dataset_raw = pd.read_csv('classifier/data/dataset_full.csv')

dataset = subset = pd.concat([
    dataset_raw.iloc[:, :4],         # Columns 0–3
    dataset_raw.iloc[:, 16:21],      # Columns 10–19
    dataset_raw.iloc[:, 30:]         # Columns 30 and beyond
], axis=1)

#feature labels and number of features for later use
feature_names = list(dataset.columns.values)[:111]
num_features = len(feature_names)

#split the csv into training data and labels
X, y = dataset.iloc[:,0:111], dataset['phishing']
print(X['time_domain_activation'])
#split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#creation of validation sets for use with feature permutation from the training sets
X_train, X_vali, y_train, y_vali = train_test_split(X_train, y_train, test_size=0.2)

#train the model
forest = sklearn.ensemble.RandomForestClassifier(random_state=0).fit(X_train, y_train);

#training predictions and accuracy
y_pred = forest.predict(X_train)

training_accuracy = sklearn.metrics.accuracy_score(y_train, y_pred)

#test predictions and accuracy
y_pred = forest.predict(X_test)

test_accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)

print('{:.2%} training accuracy'.format(training_accuracy))
print('{:.2%} training error'.format(1-training_accuracy))
print('{:.2%} test accuracy'.format(test_accuracy))
print('{:.2%} test error'.format(1-test_accuracy))

#for plotting purposes
forest_acc = [training_accuracy*100, test_accuracy*100]
