## I will consider the test set as the capture number 2 because I need to compare with a chart in NodeRed the actual
## ground truth of the capture and the prediction done by the model. Hence, the capture 3 will be my TEST DATA.

## The other captures will be my TRAINING DATA. I will divide my training data into TRAINING SET and VALIDATION SET using
## an apposite method in scikit-learn. I will not use the same method for the whole TRAINING DATASET because I need to
## have a possible comparison in NodeRed.
## TODO use an image to explain the terminology (I used the AN2DL slide)
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve

df_train = pd.concat(map(pd.read_csv, ['capture1_train.csv', 'capture3_train.csv']), ignore_index=True)   # Training dataframe
features = list(df_train.columns)[2:-1]
target = list(df_train.columns)[-1]

train_sizes = np.linspace(0,0.8,51)[1:] # The train size must be a number greater than zero, hence I exclude the first number

# Note that "learning_curve" will take care of putting aside a validation set, because we will use cross-validation.
# In fact, the function "train_test_split(X_main, y_main, test_size=0.2)" is used to create a static validation set out of the training set
# In this case, I use a 5-kfold cross-validation
# LOGISTIC REGRESSION
train_sizes, train_scores, val_scores = learning_curve(estimator = LogisticRegression(max_iter=2000), X = df_train[features],
                                                       y = df_train[target], train_sizes = train_sizes, cv = 5,
                                                       scoring = 'accuracy', shuffle=True)

print('Training scores:\n\n', train_scores)
print('\n', '-' * 70) # separator to make the output easy to read
print('\nValidation scores:\n\n', val_scores)

train_scores_mean = train_scores.mean(axis = 1)
val_scores_mean = val_scores.mean(axis = 1)
print('Mean training scores\n\n', pd.Series(train_scores_mean, index = train_sizes))
print('\n', '-' * 20) # separator
print('\nMean validation scores\n\n', pd.Series(val_scores_mean, index = train_sizes))

import matplotlib.pyplot as plt

plt.figure()
plt.style.use('seaborn')
plt.plot(train_sizes, train_scores_mean, label = 'Training accuracy')
plt.plot(train_sizes, val_scores_mean, label = 'Validation accuracy')
plt.ylabel('Accuracy', fontsize = 14)
plt.xlabel('Training set size', fontsize = 14)
plt.title('Learning curves for a logistic regression model', fontsize = 18, y = 1.03)
plt.legend()



# RANDOM FOREST
train_sizes = np.linspace(0,0.8,11)[1:]
train_sizes, train_scores, val_scores = learning_curve(estimator = RandomForestClassifier(), X = df_train[features],
                                                       y = df_train[target], train_sizes = train_sizes, cv = 5,
                                                       scoring = 'accuracy', shuffle=True)

print('Training scores:\n\n', train_scores)
print('\n', '-' * 70) # separator to make the output easy to read
print('\nValidation scores:\n\n', val_scores)

train_scores_mean = train_scores.mean(axis = 1)
val_scores_mean = val_scores.mean(axis = 1)
print('Mean training scores\n\n', pd.Series(train_scores_mean, index = train_sizes))
print('\n', '-' * 20) # separator
print('\nMean validation scores\n\n', pd.Series(val_scores_mean, index = train_sizes))


plt.figure()
plt.style.use('seaborn')
plt.plot(train_sizes, train_scores_mean, label = 'Training accuracy')
plt.plot(train_sizes, val_scores_mean, label = 'Validation accuracy')
plt.ylabel('Accuracy', fontsize = 14)
plt.xlabel('Training set size', fontsize = 14)
plt.title('Learning curves for a random forest model', fontsize = 18, y = 1.03)
plt.legend()

plt.show()