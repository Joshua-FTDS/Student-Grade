import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():

    #buka title
    st.title ('Student Grade Class Prediction')
    st.markdown ('---')

    #buat subheader
    st.subheader ('EDA to Analyze')

    #load gambar
    image = Image.open('school.jpg')
    st.image(image, caption = 'photo by: Google')

    #buka dataframe
    st.write ('## **Dataset**')
    df = pd.read_csv('Student_performance_data _.csv')
    st.dataframe(df)

    # Scatter plot between Absences and GradeClass
    st.write('## **Scatter Plot of Absences vs GradeClass with Linear Regression Line**')
    # Scatter plot between Absences and GradeClass
    fig = plt.figure(figsize=(10, 6))
    sns.regplot(x='Absences', y='GradeClass', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Scatter Plot of Absences and GradeClass')
    plt.xlabel('Absences')
    plt.ylabel('GradeClass')
    plt.grid(True)
    # Use Streamlit to display the plot
    st.pyplot(fig)
    

    # Scatter plot between StudyTimeWeekly and GradeClass
    st.write('## **Scatter Plot of StudyTimeWeekly vs GradeClass with Linear Regression Line**')
    fig = plt.figure(figsize=(10, 6))
    sns.regplot(x='StudyTimeWeekly', y='GradeClass', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Scatter Plot of StudyTimeWeekly and GradeClass')
    plt.xlabel('StudyTimeWeekly')
    plt.ylabel('GradeClass')
    plt.grid(True)
    plt.show()
    st.pyplot(fig)

    # Scatter plot between ParentalSupport and GradeClass
    st.write ('## **Scatter Plot of ParentalSupport vs GradeClass with Linear Regression Line**')
    fig = plt.figure(figsize=(10, 6))
    sns.regplot(x='ParentalSupport', y='GradeClass', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Scatter Plot of ParentalSupport and GradeClass')
    plt.xlabel('ParentalSupport')
    plt.ylabel('GradeClass')
    plt.grid(True)
    plt.show()
    st.pyplot(fig)

    st.write ('## **Pairwise Relationships Between Activities and Academic Performance**')
    image = Image.open('output.png')
    st.image(image, caption = 'photo by: Google')
    

    # Menghitung rata-rata nilai akademik berdasarkan Gender
    average_by_gender = df.groupby('Gender')['GradeClass'].mean().reset_index()
    # Visualisasi Bar Plot berdasarkan Gender
    st.write ('## **Grade Class by Gender**')
    fig = plt.figure(figsize=(8, 5))
    sns.barplot(x='Gender', y='GradeClass', data=average_by_gender, palette='Set2')
    plt.title('Rata-Rata Nilai Akademik Berdasarkan Jenis Kelamin')
    plt.xlabel('Jenis Kelamin')
    plt.ylabel('Rata-Rata Kelas Nilai')
    plt.show()
    st.pyplot(fig)

    # Menghitung rata-rata nilai akademik berdasarkan Ethnicity
    average_by_ethnicity = df.groupby('Ethnicity')['GradeClass'].mean().reset_index()
    # Visualisasi Bar Plot berdasarkan Ethnicity
    st.write ('## **Grade Class by Ethnicity**')
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x='Ethnicity', y='GradeClass', data=average_by_ethnicity, palette='Set1')
    plt.title('Rata-Rata Nilai Akademik Berdasarkan Latar Belakang Etnis')
    plt.xlabel('Latar Belakang Etnis')
    plt.ylabel('Rata-Rata Kelas Nilai')
    plt.show()
    st.pyplot(fig)


if __name__== "__main__":
    run()