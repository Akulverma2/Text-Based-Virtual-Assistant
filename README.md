🤖Text-Based Virtual Assistant with Music Recommendation

A Python-based text virtual assistant that can perform system tasks, control media, and recommend songs based on your mood using machine learning.

📌 Overview

This project is a command-line virtual assistant that interacts with users through text input. It can execute various system operations like opening apps, controlling volume and brightness, searching the web, and even recommending songs based on mood using a dataset.

The assistant combines automation + basic AI + data science to create a practical and interactive tool.

🚀 Features
💬 Basic conversation (greetings, name)
🔊 Volume control (up, down, mute)
💡 Screen brightness control
🎵 Media control (play/pause, next, previous)
🖥️ Open applications (Chrome, Notepad, Calculator, VS Code)
🌐 Web search using browser
🎧 Mood-based music recommendation system
🕒 Displays current time
🧠 Music Recommendation System

The assistant recommends songs based on mood using:

Dataset: spotify.csv
Features used:
Danceability
Energy
Valence
Tempo
Algorithm:
Feature scaling using StandardScaler
Similarity measurement using Cosine Similarity
Supported Moods:
Happy 😊
Sad 😢
Energetic ⚡
Calm 🌿
🛠️ Tech Stack
Python
Pandas & NumPy – Data handling
Scikit-learn – Machine learning
PyAutoGUI – System control
screen-brightness-control – Brightness adjustment
Webbrowser & OS modules – App & browser automation
