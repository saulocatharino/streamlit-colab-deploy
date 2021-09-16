import streamlit as st

filename = 'video.mp4'
if st.button("Play"):
    video_file = open(filename, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
