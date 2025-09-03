import streamlit as st
import pandas as pd
import pickle


def load_model():
    model_pkl_file = "randomforest_heart_91%.pkl"
    with open(model_pkl_file, 'rb') as file:  
        model = pickle.load(file)
    return model

rf_model = load_model()

def prediction_algo(rf,input_dframe):
    new_input_df = pd.DataFrame(input_dframe)
    final_ans = rf.predict(new_input_df)
    st.write(new_input_df.shape)
    return final_ans[0]

def show_pp():
    st.write("Hello Guys welcome to our prediction model")

    # Get user inputs
    age = st.number_input("How Old Are You ?", 0, 100)
    sex = st.number_input("SEX M/F [Male, Female]")
    cp = st.number_input("Chest Pain Type, [atypical angina, typical angina, non-anginal pain, asymptomatic]")
    trestbps = st.number_input("Enter Resting Blood Pressure", 0.0)
    chol = st.number_input("Enter Cholesterol Level", 0.0)
    fbs = st.number_input("Enter Fasting Blood Sugar Level", 0.0)
    restecg = st.number_input("Type of EkG, [Normal, ST-T wave abnormality, Left ventricular hypertrophy]")
    thalach = st.number_input("Enter Maximum HeartRate achieved during a stress test", 0.0)
    exang = st.number_input("Exercised Induced Angina, [yes, no]")
    oldpeak = st.number_input("Enter Old Peak", 0.0)
    slope = st.number_input("Enter Slope of the peak exercise ST segment, [Flat, Upsloping,Downsloping]")
    ca = st.number_input("Number of major vessels (0-4) colored by fluoroscopy", 0.0)
    thal = st.number_input("Enter Thalium Stress Test Result, [Normal, Fixed defect, Reversible defect]")

  
    # Create input dictionary
    input_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Display input DataFrame
    st.write("Input Data:", input_df)

    answer = prediction_algo(rf_model,input_df)
    if answer == 0:
        st.title("No Risk")
    else:
        st.title("Risk Detected")


