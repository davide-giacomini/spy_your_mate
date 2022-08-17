import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

train = pd.read_csv('capture1_train.csv')

feature_cols = train.columns.values.tolist()
feature_cols.pop(0)  # The first column is unnamed
feature_cols.pop(0) # The second column is the time interval, and it is not useful
feature_cols.pop(-1)    # column of Person

X_train = train.loc[:, feature_cols]
y_train = train.Person

classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, y_train)

test = pd.read_csv('capture2_test.csv')
X_test = test.loc[:, feature_cols]
y_test = test.Person

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

kaggle_data = pd.DataFrame({'PacketId': test.xs('Unnamed: 0', axis=1), 'Person':y_pred}).set_index('PacketId')
kaggle_data.to_csv('prediction_random_forest.csv')