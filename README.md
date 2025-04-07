# 🎵 Mood-Based Music Player using Face Emotion Detection

This project is a smart music player that automatically detects your mood using your facial expression via webcam and plays a suitable Spotify playlist based on your emotion.

It uses **DeepFace** for real-time facial emotion recognition and **Spotify API** to stream playlists that match your mood.

## 💡 Features

- 🎭 Detects emotions like **Happy, Sad, Angry, Surprise, Disgust, Fear, Neutral, Contempt**
- 🎵 Automatically plays a curated Spotify playlist based on the detected emotion
- 📷 Real-time webcam integration for facial emotion detection
- 💻 Simple and interactive GUI using Streamlit
- 🌐 Can be deployed on Streamlit Cloud and shared with others

## 🚀 How It Works

1. Webcam captures your face
2. DeepFace analyzes the facial expression and detects the **dominant emotion**
3. Based on the emotion, a matching **Spotify playlist URI** is fetched
4. Spotify Web API starts playing the playlist on your active device

## 🛠️ Technologies Used

- Python
- OpenCV
- DeepFace
- Spotipy (Spotify API)
- Streamlit (for web UI)
- Haarcascade Classifier (for face detection)

## 🧪 Sample Emotions and Playlists

| Emotion   | Spotify Playlist |
|-----------|------------------|
| Happy     | Energetic Songs Playlist |
| Sad       | Emotional/Melodic Songs |
| Angry     | Hardcore / Rock |
| Fear      | Calming / Ambient |
| Surprise  | Random Mix |
| Disgust   | Chill Vibes |
| Contempt  | Lo-fi Beats |
| Neutral   | Default Lo-fi |

## 🖥️ Local Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/emotion-music-player.git
   cd emotion-music-player
