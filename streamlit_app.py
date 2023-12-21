#streamlit_app.py

import streamlit as st

def generate_text(button_index):
    if button_index == 1:
        return "Text generated from Button 1."
    elif button_index == 2:
        return "Text generated from Button 2."
    elif button_index == 3:
        return "Text generated from Button 3."

# Streamlit app layout
st.title("Lyrics Generation App")

import streamlit as st

# Function to generate text based on the button clicked
def generate_text(button_index):
    if button_index == 1:
        return "Text generated from Button 1."
    elif button_index == 2:
        return "Text generated from Button 2."
    elif button_index == 3:
        return "Text generated from Button 3."

# Streamlit app layout
st.title("Text Generation App")

# Create a two-column layout for buttons and text areas
col1, col2 = st.beta_columns(2)

# Button 1 and Text Window 1
if col1.button("Generate Text from Button 1"):
    text1 = generate_text(1)
    col1.text_area("Generated Text (Button 1)", text1)

# Button 2 and Text Window 2
if col1.button("Generate Text from Button 2"):
    text2 = generate_text(2)
    col1.text_area("Generated Text (Button 2)", text2)

# Button 3 and Text Window 3
if col2.button("Generate Text from Button 3"):
    text3 = generate_text(3)
    col2.text_area("Generated Text (Button 3)", text3)

