# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:22:57 2025
@author: DELL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading models
diabetes_model = pickle.load(open('/home/uday/intership sav/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/home/uday/intership sav/heart_diseaseLR.sav', 'rb'))
parkinson_model = pickle.load(open('/home/uday/intership sav/ParkinsonsSVM.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index = 0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Value')
    with col2:
        Age = st.text_input('Age of the Person')

    dia_diagnosis = ''
    
    if st.button('Diabetes test result'):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diaprediction = diabetes_model.predict([input_data])

            if diaprediction[0] == 1:
                dia_diagnosis = 'The Person is Diabetic'
            else:
                dia_diagnosis = 'The Person is not Diabetic'

            st.success(dia_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:   
        sex = st.text_input('Sex (1 = male, 0 = female)')
    with col3:    
        cp = st.text_input('Chest Pain Type (0–3)')
    with col1:    
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:    
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:    
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:    
        restecg = st.text_input('Resting Electrocardiographic Results (0–2)')
    with col2:    
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:    
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    with col1:    
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:    
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:    
        ca = st.text_input('Number of Major Vessels Colored by Flourosopy (0–3)')
    with col1:    
        thal = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    if st.button('Heart Disease test result'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                float(ca), float(thal)
            ]
            heartprediction = heart_disease_model.predict([input_data])

            if heartprediction[0] == 1:
                heart_diagnosis = 'The Person has Heart Disease'
            else:
                heart_diagnosis = 'The Person does not have Heart Disease'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# Parkinsons Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson’s Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        meanfreq = st.number_input('MDVP:MeanFreq(Hz)', format="%.5f")
    with col2:
        fo = st.number_input('MDVP:Fo(Hz)', format="%.5f")
    with col3:
        fhi = st.number_input('MDVP:Fhi(Hz)', format="%.5f")
    with col4:
        flo = st.number_input('MDVP:Flo(Hz)', format="%.5f")
    with col5:
        jitter_percent = st.number_input('MDVP:Jitter(%)', format="%.5f")
    with col1:
        jitter_abs = st.number_input('MDVP:Jitter(Abs)', format="%.5f")
    with col2:
        rap = st.number_input('MDVP:RAP', format="%.5f")
    with col3:
        ppq = st.number_input('MDVP:PPQ', format="%.5f")
    with col4:
        ddp = st.number_input('Jitter:DDP', format="%.5f")
    with col5:
        shimmer = st.number_input('MDVP:Shimmer', format="%.5f")
    with col1:
        shimmer_db = st.number_input('MDVP:Shimmer(dB)', format="%.5f")
    with col2:
        apq3 = st.number_input('Shimmer:APQ3', format="%.5f")
    with col3:
        apq5 = st.number_input('Shimmer:APQ5', format="%.5f")
    with col4:
        apq = st.number_input('MDVP:APQ', format="%.5f")
    with col5:
        dda = st.number_input('Shimmer:DDA', format="%.5f")
    with col1:
        nhr = st.number_input('NHR', format="%.5f")
    with col2:
        hnr = st.number_input('HNR', format="%.5f")
    with col3:
        rpde = st.number_input('RPDE', format="%.5f")
    with col4:
        dfa = st.number_input('DFA', format="%.5f")
    with col5:
        spread1 = st.number_input('spread1', format="%.5f")
    with col1:
        spread2 = st.number_input('spread2', format="%.5f")
    with col2:
        d2 = st.number_input('D2', format="%.5f")
    with col3:
        ppe = st.number_input('PPE', format="%.5f")

    if st.button('Parkinson test result'):
        input_data = [
            meanfreq, fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
            shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
            rpde, dfa, spread1, spread2, d2, ppe
        ]

        try:
            parkprediction = parkinson_model.predict([input_data])

            if parkprediction[0] == 1:
                park_diagnosis = "The Person has Parkinson’s Disease"
            else:
                park_diagnosis = "The Person does not have Parkinson’s Disease"

            st.success(park_diagnosis)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
