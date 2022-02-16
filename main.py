#Import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

#Project Title
st.title('Disney Plus Data Visualization')

#Read the data
df=pd.read_csv('data.csv')

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

df
