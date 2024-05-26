Imagine having a helpful assistant you can talk to! This Python code brings that assistant to life, letting you control it with your voice.


Here's what it can do:
*Getting Ready (Imports).
*The code gathers tools to understand you and complete tasks.
*Speech recognition: Turns your spoken words into text the assistant can understand.
*Text-to-speech: Allows the assistant to speak back to you.
*Web browsing: Opens websites you ask for.
*Date and time: Tells you the time.
*File operations: Plays music files (if you have them).
*Web requests: Fetches weather information from the internet.


Setting Up (Initialization):
*The code prepares the tools for use.
*A listener to hear your voice commands.
*A voice to speak back the assistant's responses.


->Your Commands, Its Actions (Functions):                     
->The code defines different skills the assistant has:
speak: Takes text and reads it aloud for you.
listen: Pays attention to your voice commands and converts them to text for understanding (similar to taking dictation).
open_website: Opens any website you tell it to visit.
get_weather: Fetches the current temperature and weather condition for a city you ask about. (It needs a special key to access this information.)
get_time: Tells you the current time.
play_music: Plays any music files you have stored on your computer. (It needs to find them first.)
perform_task: This is the brain of the assistant. It understands the keywords in your voice command (like "open Youtube") and calls the appropriate skill (like "open_website") to complete your request.


Let's Talk (Main Loop):
->The assistant first greets you to start things off.
Then, it listens for your voice commands in a loop.
If it understands your command (like "play music"), it uses the perform_task function to handle your request.
The loop keeps going until you tell it to "exit".



import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests
import subprocess

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and recognize speech"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    return query.lower()

def open_website(url):
    """Open a website"""
    webbrowser.open(url)
    speak(f"Opening {url}")

def get_weather(city):
    """Fetch and speak the weather information"""
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    try:
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main = weather_data["main"]
            temperature = main["temp"]
            weather_desc = weather_data["weather"][0]["description"]
            speak(f"The temperature in {city} is {temperature - 273.15:.2f} degrees Celsius with {weather_desc}.")
        else:
            speak("City not found.")
    except Exception as e:
        speak("There was an error fetching the weather data.")

def get_time():
    """Fetch and speak the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def play_music():
    """Play music from a specified directory"""
    music_dir = 'YOUR_MUSIC_DIRECTORY_PATH'
    songs = os.listdir(music_dir)
    if songs:
        song_path = os.path.join(music_dir, songs[0])
        if os.name == 'nt':  # For Windows
            os.startfile(song_path)
        else:  # For macOS and Linux
            subprocess.call(["open" if os.name == 'posix' else "xdg-open", song_path])
        speak("Playing music.")
    else:
        speak("No music files found in the directory.")

def perform_task(query):
    """Perform tasks based on the recognized query"""
    if 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'time' in query:
        get_time()
    elif 'weather' in query:
        speak("Which city?")
        city = listen()
        if city != "None":
            get_weather(city)
    elif 'play music' in query:
        play_music()
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    speak("How can I assist you today?")
    while True:
        query = listen()
        if query and query != "None":
            perform_task(query)















                
