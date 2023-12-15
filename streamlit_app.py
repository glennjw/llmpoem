#streamlit_app.py


import streamlit as st
import pandas as pd
import numpy as np
import pickle  
#to load a saved modelimport base64  
#to open .gif files in streamlit app

# @st.cache(suppress_st_warning=True)
# def get_fvalue(val):
#   feature_dict = {"No":1,"Yes":2}
#   for key,value in feature_dict.items():
#     if val == key:
#       return value
      
# def get_value(val,my_dict):
#   for key,value in my_dict.items(): 
#     if val == key:
#       return value
      
      
# app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages



# Streamlit app
st.title("When Shakespeare meets modern singers")
st.subheader("AI lyrics generator")

# User input text area
user_input = st.text_area("Enter a starting text:", "Once upon a time in a land far away...")

# Button to generate lyrics
if st.button("Generate Lyrics"):
    # Use your model to generate lyrics based on user input
    generated_lyrics = generate_lyrics(user_input)
    st.write("Generated Lyrics:")
    st.write(generated_lyrics)
