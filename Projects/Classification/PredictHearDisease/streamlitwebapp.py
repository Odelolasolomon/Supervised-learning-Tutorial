import numpy as np
import streamlit as st
import pickle

loaded_model= pickle.load(open("C:/Users/512GB/OneDrive/Documents/Major_Files/DevCareer/Another_SupervisedML/Projects/Classification/PredictHearDisease/predictor_model.sav","rb"))


#create function for prediction
def Heart_Disease_prediction(input_data):
    
    input_data_array= np.asarray(input_data)

    input_data_array_shaped= input_data_array.reshape(1,-1)


    prediction= loaded_model.predict(input_data_array_shaped)
    print(prediction)

    if (prediction[0] ==0):
        print('Patient has no heart disease')
    else:
        print('Patient has heart disease')


def main():
    
    st.title('Predict Patients With Heart Disease')

    Age= st.text_input('Age')
    RestingBP= st.text_input('RestingBP') 
    Cholesterol= st.text_input('Cholesterol')
    MaxHR = st.text_input('MaxHR')
    Oldpeak= st.text_input('Oldpeak')
    ChestPainType_ASY= st.text_input('ChestPainType_ASY')
    ChestPainType_ATA= st.text_input('Chespaintype_ATA')
    ChestPainType_NAP= st.text_input('Chestpaintype_NAP')
    ChestPainType_TA= st.text_input('Chestpaintype_TA')
    FastingBS_0 = st.text_input('FastingsBS_0')
    FastingBS_1= st.text_input('FastingBS_1')
    RestingECG_LVH= st.text_input('RestingECG_LVH')
    RestingECG_Normal= st.text_input('RestingECG_Normal')
    RestingECG_ST= st.text_input('RestingECG_ST')
    ExerciseAngina_N= st.text_input('ExerciseAngina_N')
    ExerciseAngina_Y = st.text_input('ExerciseAngina_Y')
    ST_Slope_Flat = st.text_input('ST_Slope_Flat')
    ST_Slope_Up= st.text_input('ST_Slope_Up')

    #code for prediction
    diagnosis= ''

    #create a button
    if st.button('Patients Test Result'):
         diagnosis= Heart_Disease_prediction([Age, RestingBP, Cholesterol, MaxHR, Oldpeak,
       ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP,
       ChestPainType_TA, FastingBS_0, FastingBS_1, RestingECG_LVH,
       RestingECG_Normal, RestingECG_ST, ExerciseAngina_N,
       ExerciseAngina_Y, ST_Slope_Flat, ST_Slope_Up])
    
    st.success(diagnosis)

if __name__ == '__main__':
        main()


    
    