import streamlit as st

from utils import download_video, download_playlist, download_audio, download_audio_playlist, style


st.markdown(style(), unsafe_allow_html=True)
st.title("QuickTube")
st.text("QuickTube is a simple and easy way to download videos and audios from YouTube.")

mode = st.selectbox(
    "What do you want to download?", ["Select a Mode", "Video", "All Videos From Playlist", "Audio", "All Audios From Playlist"])

if mode == "Video":
    video_url = st.text_input("Enter Video URL")
    if video_url:
        download_video(video_url)

elif mode == "All Videos From Playlist":
    playlist_url = st.text_input("Enter Playlist URL")
    if playlist_url:
        download_playlist(playlist_url)

elif mode == "Audio":
    audio_url = st.text_input("Enter Audio URL")
    if audio_url:
        download_audio(audio_url)

elif mode == "All Audios From Playlist":
    audio_playlist_url = st.text_input("Enter Playlist URL")
    if audio_playlist_url:
        download_audio_playlist(audio_playlist_url)
