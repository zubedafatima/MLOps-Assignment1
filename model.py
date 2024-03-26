####################### Model code used from Kaggle
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('Student_Performance.csv')
data.sample(4)

data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes': 1, 'No' : 0})

X = data.drop(columns=['Performance Index'])
y = data['Performance Index']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

lr = LinearRegression()
lr.fit(X_train,y_train)

print("Model Score: ",lr.score(X_train,y_train))



# Save the trained model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(lr, file)
