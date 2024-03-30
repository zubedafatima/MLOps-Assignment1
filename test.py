import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from model import lr  # assuming lr is the LinearRegression model variable

class TestLinearRegressionModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Sample dataset for testing
        data = {
            'Extracurricular Activities': ['Yes', 'No', 'Yes', 'No'],
            'Study Hours': [10, 4, 9, 3],
            'Performance Index': [90, 50, 85, 45]
        }
        df = pd.DataFrame(data)
        df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})
        
        X = df.drop(columns=['Performance Index'])
        y = df['Performance Index']
        
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(X, y, test_size=0.2)
        cls.model = LinearRegression()
        cls.model.fit(cls.X_train, cls.y_train)

    def test_model_training(self):
        # Test if the model trains correctly
        score = self.model.score(self.X_train, self.y_train)
        self.assertTrue(0 <= score <= 1)  # Score should be between 0 and 1

    def test_model_prediction(self):
        # Test if the model can make predictions
        predictions = self.model.predict(self.X_test)
        self.assertEqual(len(predictions), len(self.X_test))  # Should predict a value for each test example

if __name__ == '__main__':
    unittest.main()