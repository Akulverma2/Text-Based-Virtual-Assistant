import webbrowser
import os
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pyautogui
import screen_brightness_control as sbc

# -----------------------------
# 🔹 Load dataset
df = pd.read_csv("spotify.csv")

features = ["danceability", "energy", "valence", "tempo"]
df = df.dropna(subset=features)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# -----------------------------
# 🔹 Mood definitions
mood_dict = {
    "happy": [0.8, 0.8, 0.9, 120],
    "sad": [0.3, 0.3, 0.2, 70],
    "energetic": [0.7, 0.9, 0.6, 140],
    "calm": [0.4, 0.3, 0.5, 80]
}

# -----------------------------
def recommend_songs(mood):
    if mood not in mood_dict:
        print("❌ Invalid mood")
        return

    mood_df = pd.DataFrame([mood_dict[mood]], columns=features)
    mood_scaled = scaler.transform(mood_df)

    similarity = cosine_similarity(mood_scaled, scaled_features)
    top_indices = similarity[0].argsort()[-10:][::-1]

    print(f"\n🎧 Top {mood.capitalize()} Songs:\n")

    for i in top_indices[:5]:
        print(f"{df.iloc[i]['track_name']} - {df.iloc[i]['artist']}")

# -----------------------------
def run_alexa():
    command = input("\nEnter command: ").lower()

    # -----------------------------
    if "hello" in command:
        print("Alexa: Hello! How can I help you?")

    elif "your name" in command:
        print("Alexa: I am your smart assistant")

    # -----------------------------
    # 🔊 Volume control
    elif "volume up" in command:
        pyautogui.press("volumeup")
        print("Volume increased")

    elif "volume down" in command:
        pyautogui.press("volumedown")
        print("Volume decreased")

    elif "mute" in command:
        pyautogui.press("volumemute")
        print("Muted")

    # -----------------------------
    # 💡 Brightness control
    elif "brightness up" in command:
        current = sbc.get_brightness()[0]
        sbc.set_brightness(min(current + 10, 100))
        print("Brightness increased")

    elif "brightness down" in command:
        current = sbc.get_brightness()[0]
        sbc.set_brightness(max(current - 10, 0))
        print("Brightness decreased")

    # -----------------------------
    # 🎵 Media control
    elif "play music" in command or "pause music" in command:
        pyautogui.press("playpause")
        print("Toggled music")

    elif "next song" in command:
        pyautogui.press("nexttrack")

    elif "previous song" in command:
        pyautogui.press("prevtrack")

    # -----------------------------
    # 🖥️ Open apps
    elif "open chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        print("Opening Chrome")

    elif "open notepad" in command:
        os.system("notepad")
        print("Opening Notepad")

    elif "open calculator" in command:
        os.system("calc")
        print("Opening Calculator")

    # Custom app example
    elif "open vscode" in command:
        os.startfile("C:\\Users\\akulv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        print("Opening VS Code")

    # -----------------------------
    # 🌐 Search
    elif "search" in command:
        query = input("What should I search? ")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        print(f"Searching for {query}")

    # -----------------------------
    # 🎧 Music recommender
    elif "music" in command or "song" in command:
        mood = input("Enter mood (happy/sad/energetic/calm): ").lower()
        recommend_songs(mood)

    # -----------------------------
    elif "time" in command:
        time = datetime.now().strftime('%H:%M')
        print("Current time:", time)

    # -----------------------------
    elif "exit" in command or "stop" in command:
        print("Goodbye!")
        return False

    else:
        print("Sorry, I didn't understand.")

    return True

# -----------------------------
# 🔹 Run loop
while True:
    if not run_alexa():
        break