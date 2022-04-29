import streamlit as st
import pandas as pd
import matplotlib as plt
# import ploty.express as px
import numpy as np


st.title('Tweet Sentinment Analysis')

st.sidebar.title("Tweetiter Analysis")
st.sidebar.header("heyy")

data=pd.read_csv('../cleaned_tweet_data.csv')


if st.checkbox("Show Data"):
    st.write(data.head(50))



st.sidebar.subheader('Tweet Analyser')