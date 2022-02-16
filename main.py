#Import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

#Read the data
df=pd.read_csv('data.csv', index_col='show_id')

#Create Navigation Bar
nav = st.sidebar.radio('Navigate', ('Home','Data','Project Info'))

#Home Page
if nav=='Home':
    #Project Title
    st.title('Disney Plus Data Visualization')
    #Plot top 30 director bar graph
    st.subheader('Top 30 Directors')
    keys = df['director'].value_counts().keys().to_list()
    values = df['director'].value_counts().to_list()
    fig = px.bar(x = keys[:30], y = values[:30], data_frame = df,  
                labels={'x': 'Directors', 'y': 'no of movies'})
    st.plotly_chart(fig)

    #Plot movie and tv show comparison pie
    st.subheader('Movie vs TV Show')
    values = df['type'].value_counts()
    keys = df['type'].unique()
    fig = px.pie(df, values=values, names=keys,color=keys, color_discrete_map={'Movie':'cyan','TV Show':'royal blue'})
    st.plotly_chart(fig)

    #Movies and tv show rating
    st.subheader('Ratings of the Movies and TV Shows')
    fig = px.histogram(data_frame=df, x = ['rating'], color = 'type')
    st.plotly_chart(fig)

    #Genre of Movies
    st.subheader('Genre of Movies')
    genre_count = df.copy()
    genre_count = pd.concat([genre_count, df['listed_in'].str.split(',', expand=True)])
    genre_count = genre_count.melt(id_vars = ['type', 'title'], value_vars = range(3), value_name = 'genre')
    genre_count = genre_count[genre_count['genre'].notna()]
    fig = px.histogram(data_frame= genre_count, x = ['genre'])
    st.plotly_chart(fig)

if nav == 'Data':
    st.title('Database')
    df

if nav == "Project Info":
    st.title('PBL Project')
    st.markdown('This Data Visualization Project is made by the following students of **TE(A)** of Zeal College Of Engineering And Research under the guidance of **_Ms Zarinabegam Mundargi_** ')
    student_data = {
        'Name':['Sarthak Ekhande', 'Husain Gadiwala', 'Srujan Garde','Srushti Gavale', 'Sakshi Gawali'],
        'Roll Number':['T211031','T211032','T211033','T211034','T211035']
    }
    student_data_df = pd.DataFrame(data=student_data)
    student_data_df.set_index('Name', inplace=True)
    st.table(student_data_df)
