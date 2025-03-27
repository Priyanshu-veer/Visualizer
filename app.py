import pandas as pd
import streamlit as st
from streamlit import file_uploader
import plotly.express as px

st.title('Interactive Data Dashboard')

file_upload = file_uploader('Upload a CSV File',type=['csv'])


if file_upload:
    df = pd.read_csv(file_upload)

    st.write('DataFrame')
    st.dataframe(df)

    column = st.selectbox("Select a column to visualize",df.columns)
    #column1 = st.selectbox("Select another column to visualize", df.columns)

    fig = px.histogram(df,x=column,title=f"Distribution of column {column}")
    st.plotly_chart(fig)
