import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreak',
                    layout='wide',
                    page_icon=':Doctor:')

# Load models
diabetes_model = pickle.load(open(r"C:\\Users\\VAMSI KRUSHNA\\OneDrive\\Documents\\predictions\\saved_models\\diabetes_model.sav", "rb"))
heart_model = pickle.load(open(r"C:\Users\\VAMSI KRUSHNA\\OneDrive\\Documents\\predictions\\saved_models\\heart_model.sav", "rb"))
parkinsons_model = pickle.load(open(r"C:\Users\VAMSI KRUSHNA\OneDrive\Documents\predictions\saved_models\parkinsons_model.sav", "rb"))

def get_float_input(input_value):
    try:
        return float(input_value)
    except ValueError:
        return None  

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System', ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson\'s Disease Prediction'],
                        menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Gluclose = st.text_input('Gluclose level')
    with col3: Bloodpressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of person')

    if st.button('Diabetes Test Result'):
        user_input = [
            get_float_input(Pregnancies), get_float_input(Gluclose),
            get_float_input(Bloodpressure), get_float_input(SkinThickness),
            get_float_input(Insulin), get_float_input(BMI),
            get_float_input(DiabetesPedigreeFunction), get_float_input(Age)
        ]

        if None in user_input:
            st.error("Please provide valid inputs for all fields.")
        else:
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1: Age = st.text_input('Age')
    with col2: sex = st.text_input('Sex')
    with col3: cp = st.text_input('Chest Pain types')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3: fbs = st.text_input('Fasting Blood sugar > 120 mg/dl')
    with col1: restecg = st.text_input('Resting Electrocardiographic results')
    with col2: thalach = st.text_input('Maximum Heart Rate achieved')
    with col3: exang = st.text_input('Exercise Induced Angina')
    with col1: oldpeak = st.text_input('ST depression induced by exercise')
    with col2: slope = st.text_input('Slope of the peak exercise ST segment')
    with col3: ca = st.text_input('Major vessels colored by fluoroscopy')
    with col1: thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    if st.button('Heart Disease Test Result'):
        user_input = [
            get_float_input(Age), get_float_input(sex), get_float_input(cp),
            get_float_input(trestbps), get_float_input(chol), get_float_input(fbs),
            get_float_input(restecg), get_float_input(thalach), get_float_input(exang),
            get_float_input(oldpeak), get_float_input(slope), get_float_input(ca),
            get_float_input(thal)
        ]

        if None in user_input:
            st.error("Please provide valid inputs for all fields.")
        else:
            heart_prediction = heart_model.predict([user_input])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(heart_diagnosis)

# Parkinson's Disease Prediction
if selected == 'Parkinson\'s Disease Prediction':
    st.title('Parkinson\'s Disease Prediction using ML')
    

