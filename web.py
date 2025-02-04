import os 
import pickle #pre-trained model loading
import streamlit as st #webapp
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction Of Disease Outbreak',
                   layout='wide',
                   page_icon='👨🏻‍⚕️')

diabetes_model=pickle.load(open(r"Training_models\diabetes_model.sav","rb"))
heart_model=pickle.load(open(r"Training_models\heart_model.sav","rb"))
parkinsons_model=pickle.load(open(r"Training_models\parkinsons_model.sav","rb"))

with st.sidebar:
    selected=option_menu('Prediction Of Disease Outbreak System', ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Disease Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number Of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with  col3:
        BloodPressure=st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
        Age=st.text_input('Age')

    diab_diagnosis=''
    if st.button('Diabetes Test Result '):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])   
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
        st.success(diab_diagnosis)


if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Gender')
    with  col3:
        cp=st.text_input('Chest pain type')
    with col1:
        trestbps=st.text_input('Resting blood pressure')
    with col2:
        chol=st.text_input('Cholestrol')
    with col3:
        fbs=st.text_input('Fasting blood sugar')
    with col1:
        restecg=st.text_input('Resting electrocardiographic results')
    with col2:
        thalach=st.text_input('Maximum heart rate achieved')
    with col3:
        exang=st.text_input('Exercise induced angina')
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope=st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca=st.text_input('Number of major vessels colored by flourosopy')
    with col1:
        thal=st.text_input('Patient Thal Levels')

    heart_diagnosis=''
    if st.button('Heart Disease Test Result '):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_model.predict([user_input])   
        if heart_prediction[0]==1:
            heart_diagnosis='The person does have disease'
        else:
            heart_diagnosis='The person does not have disease'
        st.success(heart_diagnosis)


if selected=='Parkinsons Disease Prediction':
    st.title('Parkinson Disease Prediction Using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        FoHz=st.text_input('MDVP:Fo(Hz)')
    with col2:
        FhiHz=st.text_input('MDVP:Fhi(Hz)')
    with  col3:
        FloHz=st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter=st.text_input('MDVP:Jitter(%)')
    with col2:
        JitterAbs=st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RAP=st.text_input('MDVP:RAP')
    with col1:
        PPQ=st.text_input('MDVP:PPQ')
    with col2:
        DDP=st.text_input('Jitter:DDP')
    with col3:
        Shimmer=st.text_input('MDVP:Shimmer')
    with col1:
        dB=st.text_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3=st.text_input('Shimmer:APQ3')
    with col3:
        APQ5=st.text_input('Shimmer:APQ5')
    with col1:
        APQ=st.text_input('MDVP:APQ')
    with col2:
        DDA=st.text_input('Shimmer:DDA')
    with col3:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col1:
        spread1=st.text_input('spread1')
    with col2:
        spread2=st.text_input('spread2')
    with col3:
        D2=st.text_input('D2')
    with col1:
        PPE=st.text_input('PPE')
    

    parkinsons_diagnosis=''
    if st.button('Parkinson Disease Test Result '):
        user_input=[FoHz,FhiHz,FloHz,Jitter,JitterAbs,RAP,PPQ,
                    DDP,Shimmer,dB,APQ3,APQ5,APQ,DDA,NHR,HNR,
                    RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction=parkinsons_model.predict([user_input])   
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis='The person does have disease'
        else:
            parkinsons_diagnosis='The person does not have disease'
        st.success(parkinsons_diagnosis)
