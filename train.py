#@ Setting up the necessary imports
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#@ Random seed for random state
SEED = 2020

#@ Loading the dataset 
df = pd.read_csv('dataset/red_wine_quality.csv')

#@ Setting up the target variable
y = df.pop("quality")

#@ Splitting the dataset to training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(df, y, test_size=0.2, random_state=SEED)

#@ Storing the Random Forest Regressor Model in a variable
model = RandomForestRegressor(max_depth=22, random_state=SEED)

#@ Fitting the model on our training set 
model.fit(X_train, Y_train)

#@ Storing the training set score 
train_score = model.score(X_train, Y_train) * 100

#@ Storing the test set score
test_score = model.score(X_test, Y_test) * 100

'''Creating a metrics.txt file, appending the scores
   to the file and saving the file in our workspace'''
with open('metrics.txt', 'w') as outfile:
    outfile.write("Training Score: %2.1f%%\n" % train_score)
    outfile.write("Testing Score: %2.1f%%\n" % test_score)

#@ Setting up the variables needed for plotting feature importance plot
importances = model.feature_importances_
labels = df.columns

# Creating a feature importance dataframe
feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature", "importance"])

#@ Sorting the values in descending order
feature_df =  feature_df.sort_values(by='importance', ascending = False)

#@ Plotting the image using seaborn 
ax = sns.barplot(x="importance", y="feature", data = feature_df)

#@ X axis label
ax.set_xlabel('Importance', fontsize = 18)

#@ Y axis label
ax.set_ylabel('Feature', fontsize =18)

#@ Title Label
ax.set_title('Random Forest\nFeature Importance', fontsize = 22)

#@ Automatically adjusts plot params
plt.tight_layout()

#@ Saving as a png file
plt.savefig("feature_importance.png", dpi=120)

#@ Closes the figure window
plt.close() 
