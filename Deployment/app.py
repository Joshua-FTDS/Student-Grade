import streamlit as st
import eda
import predict

page = st.sidebar.selectbox('Pilih Halaman Exploratory Data Analysis atau Prediksi', ('Exploratory Data Analysis','Prediction'))

if page == 'Exploratory Data Analysis':
    eda.run()
else:
    predict.run()