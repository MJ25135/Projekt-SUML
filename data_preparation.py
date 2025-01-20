import pandas as pd


class DataPreparation:
    def __init__(self):
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
            'activities': {'no': False, 'yes': True},
            'paid': {'no': False, 'yes': True},
            'higher': {'no': False, 'yes': True},
            'internet': {'no': False, 'yes': True},
            'romantic': {'no': False, 'yes': True},
        }

        for col, mapping in mappings.items():
            df[col] = df[col].map(mapping)
        return df
