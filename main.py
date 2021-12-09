import os
import random

# import predict

from time import sleep
import streamlit as st


# def to_mp3():
#     ...

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpapercave.com/wp/wp2326987.jpg");
        background-repeat: no-repeat;
        background-size: 1920px 1080px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
# <p align=center> <span style="font-size:60px;">TUNE</span> <span style="color:#e6b12c;font-size:80px;">AI</span></p>
<p align=center><span style="font-family:'Lucida Handwriting';font-size:30px;">LSTM based music generation AI.</span></p>
""", unsafe_allow_html=True)

st.markdown("***")

option = st.selectbox(
'Pick up any instrument...',
('Piano', 'Guitar', 'Flute', 'Harp', 'Violin'))
st.text('')

try:
    results = os.listdir(f'./outputs/{option}/')
    if st.button('Generate'):
        st.markdown("***")
        # # generating music manually 
        # instrument = option.lower()
        # predict.generate(instrument)

        # song = to_mp3()

        with st.spinner('Generating...'):
            sleep(5)
        st.text('Output:')
        op = random.choice(results)
        audio_file = open(str(f'./outputs/{option}/' + op), 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

        # downnload
        st.download_button(
            label="Download",
            file_name="AI generated.mp3",
            mime="audio/mp3",
            data= audio_file)

except FileNotFoundError:
    st.error('NOT AVAILABLE YET!!')
# for entering file path
# filename = st.text_input('Enter a file path:')
# if filename:
#     try:
#         with open(filename) as input:
#             st.text(input.read())
#     except FileNotFoundError:
#         st.error('File not found.')
