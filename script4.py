# ML algorithm

import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('train.csv')

feature_cols = train.columns.values.tolist()
feature_cols.pop(0)  # The first column is unnamed
feature_cols.pop(0) # The second column is the time interval, and it is not useful
feature_cols.pop(-1)

X = train.loc[:, feature_cols]
y = train.Person

logreg = LogisticRegression()

logreg.fit(X, y)