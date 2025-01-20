import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model (pipeline)
# If you saved it as a pickle:
with open('trained_model.pkl', 'rb') as f:
    predictor = pickle.load(f)

# If you'd rather load the exported pipeline directly from tpot_best_pipeline.py:
# from tpot_best_pipeline import exported_pipeline as predictor
# Make sure that predictor is trained before use or load training data again as needed.

st.title("Student Performance Predictor")

st.write("This app predicts the final grade (G3) based on various inputs.")

# Define the input fields for the features used by your model
# These should match the order and type of features the model expects
# From your code, the features are: ['G1', 'G2', 'failures', 'studytime', 'age', 'absences', 'Medu', 'Fedu', 'health', 'school']
# Note: 'school' is encoded as {GP:0, MS:1} in your script.

G1 = st.slider("G1 (First period grade, 0-20)", 0, 20, 10)
G2 = st.slider("G2 (Second period grade, 0-20)", 0, 20, 10)
failures = st.selectbox("Number of Past Class Failures", [0, 1, 2, 3])
studytime = st.selectbox("Weekly study time (1=<2h; 2=2-5h; 3=5-10h; 4=>10h)", [1, 2, 3, 4])
age = st.slider("Age of the Student", 15, 22, 17)
absences = st.number_input("Number of School Absences", min_value=0, max_value=100, value=5)
Medu = st.selectbox("Mother's Education (0=none, 1=primary, 2=5th-9th, 3=secondary, 4=higher)", [0,1,2,3,4])
Fedu = st.selectbox("Father's Education (0=none, 1=primary, 2=5th-9th, 3=secondary, 4=higher)", [0,1,2,3,4])
health = st.selectbox("Health (1=very bad to 5=very good)", [1,2,3,4,5])
school = st.selectbox("School: GP=0, MS=1", [0,1])

if st.button("Predict Final Grade"):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[G1, G2, failures, studytime, age, absences, Medu, Fedu, health, school]], 
                              columns=['G1', 'G2', 'failures', 'studytime', 'age', 'absences', 'Medu', 'Fedu', 'health', 'school'])
    
    # Predict using the loaded model
    prediction = predictor.predict(input_data)
    
    st.subheader("Predicted Final Grade (G3):")
    st.write(float(prediction[0]))
