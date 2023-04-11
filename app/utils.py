from pytube import YouTube, Playlist
import streamlit as st


def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    try:
        stream.download()
    except:
        st.error("An error occurred while downloading the video")
    return st.success("Video Downloaded")


def download_playlist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download()
        except:
            st.error("An error occurred while downloading the video")
    return st.success("Playlist Downloaded")


def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    try:
        stream.download()
    except:
        st.error("An error occurred while downloading the audio")
    return st.success("Audio Downloaded")


def download_audio_playlist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        try:
            video.streams.get_audio_only().download()
        except:
            st.error("An error occurred while downloading the audio")
    return st.success("Playlist Downloaded")


def style():
    default_style = """
    <style>
    # MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    return default_style
