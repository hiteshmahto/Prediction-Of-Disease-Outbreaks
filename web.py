import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np

# Set page config
st.set_page_config(
    page_title='Prediction of Disease Outbreaks',
    layout='wide',
    page_icon="⚕️"
)

# Function to load models safely
def load_model(filepath):
    try:
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        return None  # Return None instead of showing an error message

# Load models and scaler
diabetes_model = load_model("saved_models/diabetes_model.sav")
scaler = load_model("saved_models/diabetes_scaler.sav")
heart_disease_model = load_model("saved_models/heart_disease_model.sav")
parkinsons_model = load_model("saved_models/parkinsons_model.sav")

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreaks',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        menu_icon='hospital-fill',
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value="0")
    with col2:
        Glucose = st.text_input('Glucose Level', value="0")
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value', value="0")

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value', value="0")
    with col2:
        Insulin = st.text_input('Insulin Level', value="0")
    with col3:
        BMI = st.text_input('BMI Value', value="0")

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', value="0")
    with col2:
        Age = st.text_input('Age of the Person', value="0")

    diab_diagnosis = ''

    if st.button('Diabetes Test Result', disabled=diabetes_model is None or scaler is None):  # Disable button if model/scaler is missing
        try:
            user_input = np.array([
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]).reshape(1, -1)

            if diabetes_model and scaler:
                user_input_scaled = scaler.transform(user_input)
                prediction = diabetes_model.predict(user_input_scaled)
                diab_diagnosis = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
            else:
                diab_diagnosis = "Error: Model or Scaler not loaded."

        except ValueError:
            diab_diagnosis = "Invalid input. Please enter numeric values."

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    if heart_disease_model:
        st.write("Heart disease prediction model is available.")
        # Add input fields and prediction logic here
    else:
        st.warning("Heart disease prediction model is missing! Please train the model and save it.")

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction using ML')

    if parkinsons_model:
        st.write("Parkinson’s prediction model is available.")
        # Add input fields and prediction logic here
    else:
        st.warning("Parkinson’s prediction model is missing! Please train the model and save it.")
