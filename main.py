# %pip install --upgrade pip setuptools wheel
# %pip install pandas scikit-learn tpot matplotlib

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from tpot import TPOTRegressor
import matplotlib.pyplot as plt

df = pd.read_csv('data/student-mat.csv')
print(df.head)

columns_to_keep = ['G1', 'G2', 'G3', 'failures', 'studytime', 'age', 'absences', 'Medu', 'Fedu', 'health', 'school']
df = df[columns_to_keep]

print("Remaining columns:", df.columns)

df['school'] = df['school'].map({'GP': 0, 'MS': 1})

df = df.dropna()

X = df.drop('G3', axis=1)  
y = df['G3']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tpot = TPOTRegressor(generations=5, population_size=50, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)

y_pred = tpot.predict(X_test)

tpot.export('tpot_best_pipeline.py')

predictor = tpot.fitted_pipeline_

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print("\nPerformance Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R²): {r2:.4f}")

# Plot predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual G3 Scores')
plt.ylabel('Predicted G3 Scores')
plt.title('Actual vs Predicted G3 Scores')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal reference line
plt.show()