#from tensorflow.keras.models import load_model
import sys
sys.path.append("path/to/site-packages")

from deepface import DeepFace
import cv2
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import subprocess

playlist_dct = {
    'angry': 'spotify:playlist:0N7bTAuO8ejUjW2YkyZfRB',
    'happy': 'spotify:playlist:4nd7oGDNgfM0rv28CQw9WQ',
    'sad': 'spotify:playlist:2sOMIgioNPngXojcOuR4tn',
    'contempt': 'spotify:playlist:0pXAFx2awezHXQ1ZsczR6L',
    'fear': 'spotify:playlist:7HB0Ko1WWxBf1X4U34MOkA',
    'surprise': 'spotify:playlist:7vatYrf39uVaZ8G2cVtEik',
    'disgust': 'spotify:playlist:1oGsi9NfPN67JasT5S8wgI',
    'neutral': 'spotify:playlist:1oGsi9NfPN67JasT5S8wgI'
}


def detect_face(img):
    try:
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        print(dominant_emotion)

        # Draw text on image
        face_img = img.copy()
        cv2.putText(face_img, dominant_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)
        return face_img, dominant_emotion.lower()
    except Exception as e:
        print(f"DeepFace Error: {e}")
        return img, None


def play_song(mood):
    client_id = '54642f81d4c948409d2e28f76a264024'
    client_secret = '53b4ca020f2342ea93d30b4012f7f9e9'
    redirect_uri = 'http://127.0.0.1:8888/callback'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope='user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming'))

    # devices = sp.devices()
    # device_id = '15f6ecf68ffe53459d2db088fd8b4ef86aef9ed2'
    playlist_uri = playlist_dct.get(mood.lower())
    if not playlist_uri:
        print("No playlist for this mood.")
        return

    devices = sp.devices()
    print("Devices:", devices)

    # Find active device or fallback to first device
    if devices["devices"]:
        active_device = next((d for d in devices["devices"] if d["is_active"]), devices["devices"][0])
        device_id = active_device["id"]
        print("Using Device ID:", device_id)

        sp.transfer_playback(device_id, force_play=True)
        sp.start_playback(device_id=device_id, context_uri=playlist_uri)
        print("✅ Playlist started.")
    else:
        print("🚫 No active device found!")


def has_consecutive_repeats(elements, target_count=25):
    if not elements:
        return False, None
    current_element = elements[0]
    count = 1
    for element in elements[1:]:
        if element == current_element:
            count += 1
            if count == target_count:
                return True, element
        else:
            current_element = element
            count = 1
    return False, None


def open_spotify():
    executable_name = "spotify"
    subprocess.Popen(executable_name, shell=True)
    
