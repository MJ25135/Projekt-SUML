import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class Model:
    def __init__(self):
        self.model = RandomForestRegressor()
        self.trained = False
        self.data = pd.read_csv('../data/student-mat.csv')

    def load_dataset(self):
        columns_to_keep = [
            'sex', 'address', 'Pstatus', 'absences', 'traveltime', 'studytime',
            'schoolsup', 'famsup', 'activities', 'paid', 'higher', 'internet',
            'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'G1', 'G2', 'G3'
        ]
        df = self.data[columns_to_keep].dropna()

        mappings = {
            'sex': {'F': False, 'M': True},
            'address': {'U': False, 'R': True},
            'Pstatus': {'A': False, 'T': True},
            'schoolsup': {'no': False, 'yes': True},
            'famsup': {'no': False, 'yes': True},
            'paid': {'no': False, 'yes': True},
            'activities': {'no': False, 'yes': True},
            'higher': {'no': False, 'yes': True},
            'internet': {'no': False, 'yes': True},
            'romantic': {'no': False, 'yes': True},
        }
        for col, mapping in mappings.items():
            df[col] = df[col].map(mapping)
        self.data = df

    def train(self):
        y = self.data['G3']
        X = self.data.drop('G3', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=25)
        self.model.fit(X_train, y_train)
        self.trained = True

    def predict(self, input_data):
        if not self.trained:
            raise ValueError("Model is not trained!")
        return self.model.predict(input_data)
