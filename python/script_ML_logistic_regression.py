# ML algorithm
import glob
import os

import pandas as pd
from sklearn.linear_model import LogisticRegression

# TRAINING

train = pd.concat(
    map(pd.read_csv, ['capture1_train.csv', 'capture3_train.csv']), ignore_index=True)

feature_cols = train.columns.values.tolist()
feature_cols.pop(0)  # The first column is unnamed
feature_cols.pop(0) # The second column is the time interval, and it is not useful
feature_cols.pop(-1)    # column of Person

X_train = train.loc[:, feature_cols]
y_train = train.Person

logreg = LogisticRegression()

logreg.fit(X_train, y_train)


# PREDICTION

test = pd.read_csv('capture2_test.csv')
X_test = test.loc[:, feature_cols]
y_test = test.Person

y_pred = logreg.predict(X_test)

kaggle_data = pd.DataFrame({'PacketId': test.xs('Unnamed: 0', axis=1), 'Person':y_pred}).set_index('PacketId')
kaggle_data.to_csv('prediction_logistic_regression.csv')