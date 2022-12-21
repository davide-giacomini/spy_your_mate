# This comment is here because I don't usually work with AI and ML and I always forget the difference explained here:
# Cross-validation (script `script_ML_cross_validation.py`) is useful for tuning hyperparameters, i.e. which features are best for training the model.
# The validation and training accuracies of the cross-validation show us if the hyperparameters chosen are good for training, and in that case, we use those hyperparameters for training the network.
# Then, the network is trained (`script_ML_training_and_prediction.py`) using all and only the hyperparameters already chosen during the cross-validation.

# ML algorithm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# TRAINING

df_train = pd.concat(map(pd.read_csv, ['capture1_train.csv', 'capture3_train.csv']), ignore_index=True)
features = list(df_train.columns)[2:-1]
target = list(df_train.columns)[-1]

# Training data: I will call it "train"
X_train = df_train[features]  # The features data. It is from the third column (number 2 included) to the column before the last (-1 excluded)
y_train = df_train[target]    # The target data. It is the last column

logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)

randfor_model = RandomForestClassifier()
randfor_model.fit(X_train, y_train)


# PREDICTION

df_test = pd.read_csv('capture2_test.csv')
X_test = df_test[features]
y_test = df_test[target]

y_pred_logreg = logreg_model.predict(X_test)
y_pred_randfor = randfor_model.predict(X_test)


# METRICS

# Use score method to get accuracy of model
logreg_score = logreg_model.score(X_test, y_test)
print("Logistic regression score: ", logreg_score)

randfor_score = randfor_model.score(X_test, y_test)
print("Random forest score: ", logreg_score)

conf_matrix_logreg = metrics.confusion_matrix(y_test, y_pred_logreg)
print(conf_matrix_logreg)
# Plot confusion matrix
plt.figure()
sns.heatmap(conf_matrix_logreg, annot=True, fmt=".3f", linewidths=.5, square = True, cmap ='Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Log. Regr. Acc. Score: {0}'.format(logreg_score)
plt.title(all_sample_title, size = 15)

conf_matrix_randfor = metrics.confusion_matrix(y_test, y_pred_randfor)
print(conf_matrix_randfor)
# Plot confusion matrix
plt.figure()
sns.heatmap(conf_matrix_randfor, annot=True, fmt=".3f", linewidths=.5, square = True, cmap ='Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Rand. For. Acc. Score: {0}'.format(randfor_score)
plt.title(all_sample_title, size = 15)

plt.show()


# EXPORT PREDICTION TO CSV

kaggle_data_logreg = pd.DataFrame({'PacketId': df_test.xs('Unnamed: 0', axis=1), 'Person':y_pred_logreg}).set_index('PacketId')
kaggle_data_logreg.to_csv('prediction_logistic_regression.csv')

kaggle_data_randfor = pd.DataFrame({'PacketId': df_test.xs('Unnamed: 0', axis=1), 'Person':y_pred_randfor}).set_index('PacketId')
kaggle_data_randfor.to_csv('prediction_random_forest.csv')