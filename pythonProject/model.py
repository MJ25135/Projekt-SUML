import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from data_preparation import DataPreparation


class Model:
    def __init__(self):
        self.model = RandomForestRegressor()
        self.trained = False

    def train(self):
        data_prep = DataPreparation()
        df = data_prep.load_dataset()

        y = df['G3']
        X = df.drop('G3', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=25)
        self.model.fit(X_train, y_train)
        self.trained = True

    def predict(self, input_data):
        if not self.trained:
            raise ValueError("Model is not trained!")
        return self.model.predict(input_data)
