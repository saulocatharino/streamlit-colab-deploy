import streamlit as st

filename = 'video.mp4'
video_file = open(filename, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
