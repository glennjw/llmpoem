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

# Button 1 and Text Window 1
if st.button("Generate Text from Button 1"):
    text1 = generate_text(1)
    st.text_area("Generated Text (Button 1)", text1)

# Button 2 and Text Window 2
if st.button("Generate Text from Button 2"):
    text2 = generate_text(2)
    st.text_area("Generated Text (Button 2)", text2)

# Button 3 and Text Window 3
if st.button("Generate Text from Button 3"):
    text3 = generate_text(3)
    st.text_area("Generated Text (Button 3)", text3)

# Streamlit app
st.title("When Shakespeare meets modern singers")
st.subheader("AI lyrics generator")

# User input text area
user_input = st.text_area("lyrics ...")

# Button to generate lyrics
if st.button("Generate Lyrics"):
    # Use your model to generate lyrics based on user input
    generated_lyrics = generate_lyrics(user_input)
    st.write("Generated Lyrics:")
    st.write(generated_lyrics)
