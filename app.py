import streamlit as st
import cv2
from PIL import Image
import numpy as np
from functions import detect_face, play_song, has_consecutive_repeats, open_spotify

st.set_page_config(page_title="Emotion Music Player", layout="centered")
st.title("🎧 Emotion-Based Music Player")

# Store emotion history
if "emotions" not in st.session_state:
    st.session_state.emotions = []

# Webcam image input
img_file_buffer = st.camera_input("Take a picture to detect emotion 🎥")

if img_file_buffer is not None:
    # Convert to image
    image = Image.open(img_file_buffer)
    frame = np.array(image)

    st.image(frame, caption="Uploaded Image", use_container_width=True)

    # Process frame
    face_img, emotion = detect_face(frame)

    if emotion:
        st.image(face_img, caption=f"Detected Emotion: {emotion}", use_container_width=True)
        st.session_state.emotions.append(emotion)

        # Check repeat emotions
        status, final_emotion = has_consecutive_repeats(st.session_state.emotions, 5)
        if status:
            st.success(f"Detected emotion '{final_emotion}' repeatedly. Playing matching songs...")

            # Play song
            open_spotify()
            play_song(final_emotion)

            # Reset
            st.session_state.emotions = []
