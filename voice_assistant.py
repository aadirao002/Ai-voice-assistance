import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greet = "Good morning!"
    elif 12 <= hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    speak(f"{greet} I am your AI voice assistant. How can I help you today?")

def get_time():
    now = datetime.datetime.now().strftime('%H:%M')
    speak(f"The time is {now}")

def get_date():
    today = datetime.datetime.now().strftime('%A, %B %d, %Y')
    speak(f"Today is {today}")

def get_weather(city="New York"):
    api_key = "demo"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("main"):
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The weather in {city} is {desc} with a temperature of {temp} degrees Celsius.")
        else:
            speak("Sorry, I couldn't get the weather information.")
    except Exception as e:
        speak("Sorry, I couldn't get the weather information.")

def open_app(app_name):
    if "notepad" in app_name:
        os.system("notepad.exe")
        speak("Opening Notepad.")
    elif "calculator" in app_name:
        os.system("calc.exe")
        speak("Opening Calculator.")
    else:
        speak("Sorry, I can't open that application.")

def web_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def main():
    greet_user()
    while True:
        command = listen()
        if not command:
            continue
        if "time" in command:
            get_time()
        elif "date" in command:
            get_date()
        elif "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                get_weather(city)
            else:
                get_weather()
        elif "open" in command:
            if "notepad" in command:
                open_app("notepad")
            elif "calculator" in command:
                open_app("calculator")
            else:
                speak("Which application do you want to open?")
        elif "search for" in command:
            query = command.split("search for")[-1].strip()
            if query:
                web_search(query)
            else:
                speak("What do you want to search for?")
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't help with that yet.")

if __name__ == "__main__":
    main() 