from select import select
import streamlit as st
import pandas as pd
import matplotlib as plt
# import ploty.express as px
import numpy as np


st.title('Twitter Data Analysis')

st.sidebar.title("Tweetiter Analysis")
st.sidebar.header("heyy")

data=pd.read_csv('../cleaned_tweet_data.csv')


if st.checkbox("Show Data"):
    st.write(data.head(50))

select=st.sidebar.selectbox('Models',['Topic Model','Sentiment Analysis'])

if select == "Sentiment Analysis":

    st.sidebar.subheader('Tweet Analyser')
    tweets=st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
    polarity=st.write(data.query('polarity==0')[['original_text']].sample(1).iat[0,0])

    visualizers=st.sidebar.radio('Visualization of tweets',['Bar Chart','Pie Chart'])

    if tweets == "positive":
        polarity=st.write(data.query('polarity>0')[['original_text']].head(5))
    elif tweets == "negative":
        polarity=st.write(data.query('polarity<0')[['original_text']].head(5))
    else:
        polarity=st.write(data.query('polarity==0')[['original_text']].head(5))
else:

    st.write("no data")
