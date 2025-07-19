import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime
import wikipedia
import pywhatkit
import webbrowser
import pyjokes
import requests
import os

# Talk function using gTTS
def talk(text):
    print(f"🤖 Assistant: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

# Greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Good morning!")
    elif 12 <= hour < 18:
        talk("Good afternoon!")
    else:
        talk("Good evening!")
    talk("Hi! I'm Naruto, your voice assistant. How can I help you today?")

# Listen to the user
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🧠 Recognizing...")
        command = r.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except:
        talk("Sorry, I couldn't understand. Please say it again.")
        return ""

# Get weather (from wttr.in)
def get_weather(city="Chennai"):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        return response.text
    except:
        return "Unable to get weather info."

# Main assistant logic
def run_voice_assistant():
    greet_user()
    while True:
        command = listen()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            talk(f"Today is {date}")

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, sentences=2)
            talk(info)

        elif 'play' in command:
            song = command.replace('play', '')
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            talk("Opening Google")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)

        elif 'weather' in command:
            city = "Chennai"
            talk(f"Getting weather for {city}")
            weather_info = get_weather(city)
            talk(weather_info)

        elif 'shutdown' in command:
            talk("Shutting down the system. Goodbye!")
            os.system("shutdown /s /t 1")

        elif 'restart' in command:
            talk("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif 'your name' in command:
            talk("My name is Naruto. Your smart assistant.")

        elif 'exit' in command or 'bye' in command or 'stop' in command:
            talk("Goodbye! Have a great day!")
            break

        elif command != "":
            talk("Sorry, I didn't get that. Could you say it again?")

# Run the assistant
run_voice_assistant()
