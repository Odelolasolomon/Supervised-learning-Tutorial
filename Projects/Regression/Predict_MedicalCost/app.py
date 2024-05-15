import numpy as np
import pickle
import streamlit as st




def medical_predictor(data):
    arrayed_data= np.asarray(data)
    shaped_data= arrayed_data.reshape(1,-1)

    prediction= model.predict(data)
    print(prediction)


def main():

    st.title('Hospital Medical Charges Predictor' )

    Age= st.text_input('Patient Age')
    Patient_bmi= st.text_input('Patient_Bmi')
    children= st.text_input('have_children?')
    sex_female= st.text_input('Gender is female?')
    sex_male= st.text_input('Gender is male?')
    smoker_yes= st.text_input('Smoker yes')
    smoker_no= st.text_input('Smoker no')
    region_northeast= st.text_input('region northeast')
    region_northwest= st.text_input('region northwest')
    region_north_southeast= st.text_input('region_north_southeast')
    region_southeast= st.text_input('region_southeast')
    region_southwest= st.text_input('region_southwest')

predictor= ''

