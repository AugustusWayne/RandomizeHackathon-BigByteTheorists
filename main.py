import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pickle
import os.path    
import winshell
import pyjokes
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from ecapture import ecapture as ec
import os
import pyttsx3
import speech_recognition as sr
import gui
global window
window = gui.GUI()
global img_win
img_win = 0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    askname = ("Aura")
    speak("I am your Personal Assistant")
    speak(askname)
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    speak("How can i Help you, Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =0.5
        audio = r.listen(source)
        window.set_status("Processing...", "red")

    try:
        q = r.recognize_google(audio, language='en-in')
        window.msg_box.delete('1.0', gui.END)
        window.msg_box.update()
        print("User said :", q)
        window.set_msg(f"User said :{q}")
        process(q)

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "Default User"

    return q

def take():
    speak("Aura Online")
    window.set_msg("Aura Online...")
    while True:
        takeCommand()

def process(q):
    global window
    global img_win
    global askname

    query = q.lower()
    # All the commands said by user will be
    # stored here in 'query' and will be
    # converted to lower case for easily
    # recognition of command
    if "who are you" in query:
        speak("I am Aura, your personal virtual assistant created by BigByteTheorists")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        print("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        window.set_msg("According to wikipedia...")
        window.set_msg(f"{results}")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        print("Opening YouTube..")
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        window.set_msg("Opening YouTube..")

    elif 'open google' in query:
        print("Opening Google..")
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
        window.set_msg("Opening Google..")

    elif 'open stack overflow' in query:

        speak("Here you go to Stack Overflow. Happy coding")
        webbrowser.open("stackoverflow.com")
        window.set_msg("Opening Stack Overflow..")

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        webbrowser.open("https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg")
        window.set_msg("Playing Music")

    elif 'tell me the time'.lower() in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sure, the time is {strTime}")
        window.set_msg(strTime)

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        window.set_msg("I am fine, Thank you")
        speak("How are you?")
        window.set_msg("How are you?")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")
        window.set_msg("It's good to know that your fine")

    elif "change my name to" in query:
        query = query.replace("change my name to", "")
        askname = query

    elif "change name" in query:
        speak("What would you like to call me ")
        askname = takeCommand()
        speak("Thanks for naming me")
        window.set_msg("Thanks for naming me")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        window.set_msg("Thanks for giving me your time")
        exit()

    elif "who made you" in query or "who created you" in query:
        speak("I was created by The Big Byte Theorists.")
        window.set_msg("I was created by The Big Byte Theorists.")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif "make a google search" in query:
        speak("What do you want me to search")
        question=takeCommand()
        app_id = "LT459W-8LVHQ87PW6"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        # Includes only text from the response
        answer = next(res.results).text
        window.set_msg(answer)
        speak(answer)


    elif 'search' in query or 'play' in query:
        window.set_msg("now searching")
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif 'who am i' in query:
        speak("If you talk then definitely your human.")
        window.set_msg("If you talk then definitely your human.")

    elif 'why were you created' in query:
        speak("To help you")
        window.set_msg("To help you")

    elif 'what is love' in query:
        speak("It is the 7th sense that destroy all other senses")
        window.set_msg("It is the 7th sense that destroy all other senses")

    elif 'open maps' in query:
        speak("Here you go to Google Maps\n")
        webbrowser.open("https://www.google.com/maps")
        window.set_msg("Here you go to Google Maps")

    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
        window.set_msg("locking the device")

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")
        window.set_msg("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop Aura from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        window.set_msg("Now Locating...")
        webbrowser.open("https://www.google.com/maps/search/" + location + "")

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Aura Camera ", "img.jpg")
        window.set_msg("Say Cheese!!")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])
        window.set_msg("Now Restarting...")

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")
        window.set_msg("Going Dark")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand()
        file = open('aura.txt', 'w')
        speak("Sir, Should i include date and time")
        snmp = takeCommand()
        if 'yes' in snmp or 'sure' in snmp:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
        file.close()

    elif "show note" in query:
        speak("Showing Notes")
        file = open("aura.txt", "r")
        print(file.read())
        speak(file.read(6))

    elif "news" in query:
        main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=caa09eb1c9ca4e838a9230693ebba902'

        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")

    elif "weather" in query:

        # Google Open weather website
        # to get API of Open weather
        api_key = "006e9c57bf003ca6d75a843a104ba3ac"
        speak(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city_name,api_key)
        response = requests.get(complete_url)

        if response.status_code == 200:
            x=response.json()
            y = x['main']
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak("Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidity) + "\n description = " + str(weather_description))
            window.set_msg("Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidity) + "\n description = " + str(weather_description))

        else:
            speak(" City Not Found ")

    elif "Good Morning" in query:
        speak("A warm" + query)
        speak("How are you")
        speak(askname)

    # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:
        window.set_msg("I'm not sure about, may be you should give me some time")
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query or "how r u" in query:
        window.set_msg("I'm fine, glad you me that")
        speak("I'm fine, glad you me that")

    elif "i love u" in query or "i love you" in query:
        window.set_msg("It's hard to understand")
        speak("It's hard to understand")

    elif "what is" in query or "who is" in query:

        client = wolframalpha.Client("LT459W-8LVHQ87PW6")
        res = client.query(query)
        try:
            print(next(res.results).text)
            window.set_msg(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            window.set_msg("No Results")

if __name__ == '__main__':
    window_width = 400  # width of window
    window_height = 400  # height of window

    window.geometry(f"{window_width}x{window_height}")
    window.title("Aura - Voice Assistant")

    b1 = gui.Button(window.background_label, text="Activate Aura", command=take)
    b1.pack()

    window.create_statusbar_msgbox()
    window.set_status("Ready", "blue")

    window.mainloop()
