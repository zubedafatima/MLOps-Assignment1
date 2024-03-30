
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the data from CSV file
data = pd.read_csv('Student_Performance.csv')

# Map 'Yes' and 'No' to 1 and 0 in the 'Extracurricular Activities' column
data['Extracurricular Activities'] = data['Extracurricular Activities'].map(
    {'Yes': 1, 'No': 0})

# Split the data into features (X) and target variable (y)
X = data.drop(columns=['Performance Index'])
y = data['Performance Index']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize and train the Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Print the model score
print("Model Score: ", lr.score(X_train, y_train))

# Save the trained model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(lr, file)

print("Model created and saved into pickle file")
