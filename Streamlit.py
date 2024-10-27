import streamlit as st
import pandas as pd
import pickle

# Load your model
model_path = "./heart_disease_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the app layout
st.title("Heart Disease Prediction")
st.write("Enter the patient's data")

# Age input and mapping to age categories
age = st.sidebar.number_input("Enter Age", min_value=0, max_value=120, value=40)

# Initialize age category columns
age_inputs = [0] * 7  # 7 age categories

# Determine age category based on the input age
if age >= 80:
    age_inputs[0] = 1  # AgeCategory_80 or older
elif 75 <= age <= 79:
    age_inputs[1] = 1  # AgeCategory_75-79
elif 70 <= age <= 74:
    age_inputs[2] = 1  # AgeCategory_70-74
elif 40 <= age <= 44:
    age_inputs[3] = 1  # AgeCategory_40-44
elif 30 <= age <= 34:
    age_inputs[4] = 1  # AgeCategory_30-34
elif 25 <= age <= 29:
    age_inputs[5] = 1  # AgeCategory_25-29
else:
    age_inputs[6] = 1  # AgeCategory_35-39

# General Health input and mapping
gen_health = st.sidebar.selectbox("General Health", ["Poor", "Fair", "Very good"])
gen_health_inputs = [0, 0, 0]  # Initialize general health categories

# Map user selection to the corresponding general health category
if gen_health == "Poor":
    gen_health_inputs[0] = 1
elif gen_health == "Fair":
    gen_health_inputs[1] = 1
elif gen_health == "Very good":
    gen_health_inputs[2] = 1

# Other feature inputs
input_features = {
    "DiffWalking": st.sidebar.selectbox("Difficulty Walking?", [0, 1]),
    "Diabetic_Yes": st.sidebar.selectbox("Diabetic", [0, 1]),
    "Stroke": st.sidebar.selectbox("Stroke History?", [0, 1]),
    "PhysicalHealth": st.sidebar.slider("Physical Health Rating (0-30)", 0, 30, 5),
    "KidneyDisease": st.sidebar.selectbox("Kidney Disease?", [0, 1]),
    "Smoking": st.sidebar.selectbox("Smoker?", [0, 1]),
    "Sex": st.sidebar.selectbox("Sex (Male=1, Female=0)", [0, 1]),
    "SkinCancer": st.sidebar.selectbox("Skin Cancer", [0, 1]),
    "PhysicalActivity": st.sidebar.selectbox("Physically Active", [0, 1]),
}

# Combine input features with age and general health encoding
input_values = list(input_features.values()) +  gen_health_inputs + age_inputs 

# Define the expected columns for the DataFrame
expected_columns = list(input_features.keys()) + [
    "GenHealth_Poor",
    "GenHealth_Fair",
    "GenHealth_Very good",
    "AgeCategory_80 or older", 
    "AgeCategory_75-79", 
    "AgeCategory_70-74", 
    "AgeCategory_40-44", 
    "AgeCategory_30-34", 
    "AgeCategory_25-29", 
    "AgeCategory_35-39",

]

# Dataframe for model input
input_df = pd.DataFrame([input_values], columns=expected_columns)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("Prediction: High Risk of Heart Disease")
    else:
        st.success("Prediction: Low Risk of Heart Disease")
