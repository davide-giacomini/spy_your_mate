# ML algorithm

import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('capture1_train.csv')

feature_cols = train.columns.values.tolist()
feature_cols.pop(0)  # The first column is unnamed
feature_cols.pop(0) # The second column is the time interval, and it is not useful
feature_cols.pop(-1)    # column of Person

X = train.loc[:, feature_cols]
y = train.Person

logreg = LogisticRegression()

logreg.fit(X, y)

test = pd.read_csv('capture2_test.csv')
X_new = test.loc[:, feature_cols]

new_pred_class = logreg.predict(X_new)

kaggle_data = pd.DataFrame({'PacketId': test.xs('Unnamed: 0', axis=1), 'Person':new_pred_class}).set_index('PacketId')
kaggle_data.to_csv('sub.csv')