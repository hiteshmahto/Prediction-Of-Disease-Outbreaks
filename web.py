import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title='🩺 Disease Prediction System', layout='wide', page_icon="🧑‍⚕️")

# Load Models
diabetes_model = pickle.load(open(r"C:\Users\user\Desktop\Prediction-Of-Disease-Outbreaks\saved_models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\user\Desktop\Prediction-Of-Disease-Outbreaks\saved_models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\user\Desktop\Prediction-Of-Disease-Outbreaks\saved_models\parkinsons_model.sav", 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        '🩺 Disease Prediction System',
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction Using ML')
    st.write("### Enter the details below to predict Diabetes 🩺")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('🤰 Number of Pregnancies')
    with col2:
        Glucose = st.text_input('🩸 Glucose Level')
    with col3:
        BloodPressure = st.text_input('💉 Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('🩹 Skin Thickness')
    with col2:
        Insulin = st.text_input('💊 Insulin Level')
    with col3:
        BMI = st.text_input('⚖️ BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('🧬 Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('🎂 Age')
        
    diab_diagnosis = ''
    if st.button('🔍 Get Diabetes Test Result'):
          user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
          user_input = [float(x) for x in user_input]
          diab_prediction = diabetes_model.predict([user_input])
          if diab_prediction[0] == 1:
              diab_diagnosis = '⚠️ The person **has diabetes!** 🩸'
          else:
             diab_diagnosis = '✅ The person **does not** have diabetes! 😊'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction Using ML')
    st.write("### Enter the details below to predict Heart Disease 🫀")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('🎂 Age')
    with col2:
        Sex = st.text_input('⚧️ Sex')
    with col3:
        cp = st.text_input('💖 Chest Pain Type (cp)')
    with col1:
        trestbps = st.text_input('💉 Resting Blood Pressure (trestbps)')
    with col2:
        chol = st.text_input('🧪 Serum Cholesterol (chol)')
    with col3:
        fbs = st.text_input('🍬 Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.selectbox('🩺 Resting ECG Results', [0, 1, 2])
    with col2:
        thalach = st.text_input('🏃 Maximum Heart Rate (thalach)')
    with col3:
        exang = st.text_input('💪 Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('📉 ST Depression Induced by Exercise')
    with col2:
        slope = st.selectbox('📈 Slope of Peak Exercise ST Segment', [0, 1, 2])
    with col3:
        ca = st.selectbox('🩸 Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3])
    with col1:
        thal = st.text_input('💓 Thalassemia: 0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect')

        
    heart_diagnosis = ''

    if st.button('🔍 Get Heart Disease Test Result'):
        user_input = [Age, Sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = '⚠️ The person **has heart disease!** 🫀'
        else:
            heart_diagnosis = '✅ The person **does not** have heart disease! ❤️'
    st.success(heart_diagnosis)

# Parkinson’s Prediction Page
if selected == "Parkinson's Prediction":
    st.title("🧠 Parkinson's Disease Prediction Using ML")
    st.write("### Enter the details below to predict Parkinson's Disease 🤖")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        MDVP_Fo = st.text_input('🎤 MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('📈 MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('📉 MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter = st.text_input('📊 MDVP:Jitter(%)')
    with col1:
        MDVP_Jitter_Abs = st.text_input('📊 MDVP:Jitter(Abs)')
    with col2:
        MDVP_RAP = st.text_input('📊 MDVP:RAP')
    with col3:
        MDVP_PPQ = st.text_input('📊 MDVP:PPQ')
    with col4:
        Jitter_DDP = st.text_input('📊 Jitter:DDP')
    with col1:
        MDVP_Shim = st.text_input('📊 MDVP:Shimmer')
    with col2:
        Shimmer_db = st.text_input('📊 MDVP:Shimmer(db)')
    with col3:
        Shimmer_APQ3 = st.text_input('📊 Shimmer:APQ3')
    with col4:
        Shimmer_APQ5 = st.text_input('📊 Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('📊 MDVP:APQ5')
    with col2:
        Shimmer_DDA = st.text_input('📊 Shimmer:DDA')
    with col3:
        NHR = st.text_input('🔊 NHR')
    with col4:
        HNR = st.text_input('🎼 HNR')
    with col1:
        RPDE = st.text_input('📡 RPDE')
    with col2:
        DFA = st.text_input('📡 DFA')
    with col3:
        spread1 = st.text_input('📉 spread1')
    with col4:
        spread2 = st.text_input('📉 spread2')
    with col1:
        D2 = st.text_input('🔢 D2')
    with col2:
        PPE = st.text_input('🔢 PPE')

    Parkinsons_diagnosis = ''

    if st.button('🔍 Get Parkinson\'s Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shim, Shimmer_db, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        Parkinsons_prediction = parkinsons_model.predict([user_input])

        if Parkinsons_prediction[0] == 1:
            Parkinsons_diagnosis = '⚠️ The person **has Parkinson\'s disease!** 🧠'
        else:
            Parkinsons_diagnosis = '✅ The person **does not** have Parkinson\'s disease! 😊'

    st.success(Parkinsons_diagnosis)

# Styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: #ffffff;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #D43F3F;
    }
    .stSidebar {
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)
