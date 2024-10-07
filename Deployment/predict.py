import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json


with open('rf.pkl', 'rb') as file_1:
  model = pickle.load(file_1)


def run():
    with st.form('Student_Grade'):
        # Input fields
        student_id = st.number_input('StudentID', min_value=0, max_value=1000000000, value=0)
        age = st.number_input('Age', min_value=14, max_value=20, value=15)
        gender = st.selectbox('Gender', (0, 1), index=1, help = '0: Male ; 1: Female')
        ethnicity = st.selectbox('Ethnicity', (0, 1, 2, 3), index=1, help = '0: Caucasian ; 1: African American ; 2: Asian ; 3: Other')
        parental_education = st.selectbox('Parental Education', (0, 1, 2, 3, 4), index=2, help = "0: None ; 1: High School ; 2: Some College ; 3: Bachelor's ; 4: Higher")
        study_time_weekly = st.number_input('Study Time Weekly (hours)', min_value=0, value=0)
        absences = st.number_input('Absences', min_value=0, max_value=0, value=0)
        tutoring = st.selectbox('Tutoring', (0, 1), index=0, help = '0: No ; 1: Yes')
        parental_support = st.selectbox('Parental Support', (0, 1, 2, 3, 4), index=0, help = '0: None ; 1: Low ; 2: Moderate ; 3: High ; 4: Very High)')
        extracurricular = st.selectbox('Extracurricular', (0, 1), index=0, help = '0: No ; 1: Yes')
        sports = st.selectbox('Sports', (0, 1), index=0, help = '0: No ; 1: Yes')
        music = st.selectbox('Music', (0, 1), index=0, help = '0: No ; 1: Yes')
        volunteering = st.selectbox('Volunteering', (0, 1), index=0, help = '0: No ; 1: Yes')

        #define submit button form
        submitted = st.form_submit_button('Predict')

    data_inf = {
    'StudentID': student_id,
    'Age': age,
    'Gender': gender,
    'Ethnicity': ethnicity,
    'ParentalEducation': parental_education,
    'StudyTimeWeekly': study_time_weekly,
    'Absences': absences,
    'Tutoring': tutoring,
    'ParentalSupport': parental_support,
    'Extracurricular': extracurricular,
    'Sports': sports,
    'Music': music,
    'Volunteering': volunteering,
    }


    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # Predict with the model
    prediction = model.predict(data_inf)
    st.write('Prediction:', prediction[0])

if __name__ == '__main__':
   run()