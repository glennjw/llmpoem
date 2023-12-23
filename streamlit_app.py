#streamlit_app.py

import torch
import streamlit as st
import pandas as pd
from BigramLanguageModel import BigramLanguageModel, Block, MultiHeadAttention, Head, FeedFoward



#st.set_page_config(page_title="Speech-to-Text Transcription & ChatGPT", layout="wide", page_icon="🎤")
# Add a custom CSS style for the button

device = 'cuda' if torch.cuda.is_available() else 'cpu'

no2model = {
     1: "shakespeare",
     2: "modern",
     3: "mix"
}


def decoder(text):
    # here are all the unique characters that occur in this text
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    # create a mapping from characters to integers
    #stoi = { ch:i for i,ch in enumerate(chars) }
    itos = { i:ch for i,ch in enumerate(chars) }
    #encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
    decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output     a string
    return decode

def parser():
    shakespeare, new_lyrics = '', ''
    
    with open('dataset/shakespeare.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [s.rstrip('\n') for s in lines]
        lines = [s for s in lines if not s.endswith(":")]
        lines = [s for s in lines if s!='']
        shakespeare = ' '.join(lines)
    
    new_lyrics = pd.read_csv('dataset/modern_lyrics.csv')
    new_lyrics = ' '.join(new_lyrics['lyrics'])
    
    decode = {1:decoder(shakespeare),
              2:decoder(new_lyrics),
              3:decoder(new_lyrics + ' '+ shakespeare)
    }
    return decode




def gen(model):
    preM = no2model[model]
    #print('model: gen ', preM)

    preM = torch.load("models/"+preM+".pth")
    vocab_size = 64
    if 1==model:
        vocab_size = 64
    elif 2==model:
        vocab_size = 670
    elif 3==model:
        vocab_size = 707
    m = BigramLanguageModel(vocab_size)
    m.load_state_dict(preM)
    
    # generate from the model
    context = torch.zeros((1, 1), dtype=torch.long, device=device)
    text = parser()[model](m.generate(context, max_new_tokens=500)[0].tolist())
    if 1==model:
        replacement_dict = {';':'\n', '?':'\n', '.':'\n', '!':'\n'}
        for old_char, new_char in replacement_dict.items():
            text = text.replace(old_char, new_char)
    else:
        text = list(text)
        for i in range(len(text)):
            if text[i]==' ' and i%15==0:
                text[i] = '\n'
        text = ''.join(text)
    return text


def generate_text(button_index):
    text = gen(button_index)
    return text


# Streamlit app layout
st.title("Lyrics Generation")
st.subheader("")

col11, col12, col13 = st.columns([2,2,4])
col21, col22, col23 = st.columns([2,2,4])
col31, col32, col33 = st.columns([2,2,4])


if 'clickedc1' not in st.session_state:
       st.session_state.clickedc1 = False
if 'clickedc2' not in st.session_state:
       st.session_state.clickedc2 = False
if 'clickedc3' not in st.session_state:
       st.session_state.clickedc3 = False


def a():
    text1 = generate_text(1)
    st.session_state.clickedc1 = text1
    #col13.empty()
    col13.write(text1)


def b():
    text2 = generate_text(2)
    st.session_state.clickedc2 = text2
    #col23.empty()
    col23.write(text2)


def c():
    text3 = generate_text(3)
    st.session_state.clickedc3 = text3
    #col32.empty()
    col33.text(text3)


with col12:
    if st.session_state.clickedc1:
        col13.text(st.session_state.clickedc1)
    runButton = st.button(" Shakespeare ", on_click=a)


with col22:
    if st.session_state.clickedc2:
        col23.text(st.session_state.clickedc2)
    runButton = st.button("Modern lyrics",on_click=b)


with col32:
    if st.session_state.clickedc3:
        col33.text(st.session_state.clickedc3)
    runButton = st.button("   Mix   ",on_click=c)

# image

with col11:
    st.image("img/shakespeare.jpg", use_column_width=True)  # Replace "your_image.png" with the path to your image

with col21:
    st.image("img/singer.jpg", use_column_width=True)  # Replace "your_image.png" with the path to your image

with col31:
    st.image("img/ai_singer.jpeg", use_column_width=True)  # Replace "your_image.png" with the path to your image

