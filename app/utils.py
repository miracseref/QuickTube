from pytube import YouTube, Playlist
import streamlit as st
import os
import platform


def get_download_path():
    if platform.system() == "Windows":
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        download_path = os.path.join(os.getcwd(), "downloads")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    return download_path


# def download_video(url):
#     yt = YouTube(url)
#     stream = yt.streams.get_highest_resolution()
#     try:
#         download_path = get_download_path()
#         # Download button
#         if st.button("Download"):
#             stream.download(download_path)
#             st.write("Video downloaded successfully at", download_path)
#     except:
#         st.error("An error occurred while downloading the video")
#     return st.success("Video Downloaded")

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    try:
        download_path = get_download_path()
        stream.download(download_path)
    except:
        st.error("An error occurred while downloading the video")
    return st.success("Video Downloaded in your 'Downloads' folder.")


def download_playlist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        try:
            download_path = get_download_path()
            video.streams.get_highest_resolution().download(download_path)
        except:
            st.error("An error occurred while downloading the video")
    return st.success("Playlist Downloaded")


def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    try:
        download_path = get_download_path()
        stream.download(download_path)
    except:
        st.error("An error occurred while downloading the audio")
    return st.success("Audio Downloaded")


def download_audio_playlist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        try:
            download_path = get_download_path()
            video.streams.get_audio_only().download(download_path)
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
