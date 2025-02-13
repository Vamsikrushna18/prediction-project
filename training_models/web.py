import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='prediction of disease outbreak',
                    layout = 'wide',
                    page_icon = ':Doctor:')
diabetes_model = pickle.load(open(r"C:\\Users\\VAMSI KRUSHNA\\OneDrive\\Documents\\predictions\\saved_models\\diabetes_model.sav", "rb"))
heart_model=pickle.load(open(r"C:\Users\\VAMSI KRUSHNA\\OneDrive\\Documents\\predictions\\saved_models\\heart_model.sav" , "rb"))


with st.sidebar:
    selected=option_menu('prediction of disease of outbreak system',['Diabetes Prediction','Heart Disease Prediction'],
                        menu_icon='hospital-fill',icons=['activity','heart','person',],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Gluclose= st.text_input('Gluclose level')
    with col3:
        Bloodpressure= st.text_input('Bloodpressure value')
    with col1:
        SkinThickness= st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Imsulin level')
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of person')

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Gluclose, Bloodpressure, SkinThickness, Insulin, 
                        BMI , DiabetesPedigreeFunction, Age]
    user_input=[float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= 'The Person is diabetic'
    else:
        diab_diagnosis= 'The Person is not diabetic'
        st.success(diab_diagnosis)


if selected =='Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:

         age = st.text_input('Age') 

    with col2:

        sex = st.text_input('sex')

    with col3:

     cp = st.text_input('Chest Pain types')

    with col1:

        trestbps =  st.text_input('Resting Blood Pressure')

    with col2:

        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:

        fbs = st.text_input('Fasting Blood sugar > 120 mg/dl')

    with col1:

        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:

        thalach =  st.text_input('Maximum Heart Rate achieved')

    with col3:

        exang = st.text_input('Exercise Induced Angina')

    with col1:

        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:

        slope = st.text_input('slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')



heart_diagnosis=''





if st.button('Heart Disease Test Result'):

    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    user_input=[float(x) for x in user_input]

    heart_prediction = heart_model.predict([user_input])

    if heart_prediction[0] == 1:

         heart_diagnosis = 'The person is having heart disease' 
    else:

         heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
        