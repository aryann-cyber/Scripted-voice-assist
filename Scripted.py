import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from datetime import date
import datetime
import subprocess
import pywhatkit
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def quitSelf():
    speak("do u want to switch off the computer ")
    # Input voice command
    take = takeCommand()
    choice = take
    if choice == 'yes':
        speak("Shutting the computer")
    os.system("shutdown /s /t 10")
    if choice == 'no':
        speak("thank you sir")


def openapp():
    if 'word' in query:
        subprocess.Popen("C:\\Program Files\\MicrosoftOffice\\root\\Office16\\WINWORD.EXE")

    def closeapp():
        if 'close word' in query:
            os.system("TASKKILL /F /IM WINWORD.EXE")


def music():
    speak("which song you want to play.. hindi song.. or english song")
    take = takeCommand()
    choice = take
    if choice == 'Hindi song':
        speak("playing hindi song")
    music_dir = 'D:\\Songs\\Hindi Songs'
    songs = os.listdir(music_dir)
    print(songs)
    n = int
    n = (random.randint(0, 4))
    os.startfile(os.path.join(music_dir, songs[n]))
    if choice == 'English song':
        speak("playing english song")
    music_dir = 'D:\\Songs\\English Songs'
    songs = os.listdir(music_dir)
    print(songs)
    m = int
    m = (random.randint(0, 5))
    os.startfile(os.path.join(music_dir, songs[m]))


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am eve..... your personal assistant. Please tell me.. how may I help you")

def takeCommand():

    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I Am Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Wait.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
    # print(e)
        print("Say that again please...")
        return "None"
        return query


    if __name__ == "__main__":
         wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music()
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
        codePath ="C:\\Users\\Aryan\\PycharmProjects\\firstProject\\hello.py"
        os.startfile(codePath)
    elif 'open erp' in query:
        webbrowser.open("http://gnioterp.com:155/")
    elif 'open video' in query:
        video_dir = 'D:\\chill'
        video = os.listdir(video_dir)
        print(video)
        r = int
        r = (random.randint(0, 4))
        os.startfile(os.path.join(video_dir, video[r]))
    elif 'shutdown the computer' in query:
        quitSelf()
    elif 'ok bye' in query:
        speak("ok..sir...hope..you..enjoyed ")
        os.exit()
    elif 'which day is today' in query:
        today = date.today()
        speak(f"Today's date is.. {today} ")
    elif 'open word' in query:
        speak("ok..sir..opening..word for you..")
        openapp()
    elif 'close word' in query:
        speak("ok..sir..closing word for you")
        closeapp()
# elif 'send message' in query:
# speak("what is the message")
# content = takeCommand()
# to = input("enter your phone number with country code")
# t = input("enter the hour")
# tt = input("enter the min")
# pywhatkit.sendwhatmsg(to, content,)
    elif 'tell me about yourself' in query:
        print("my name is eve.. i am a personal assistant.. my creator is mr.aarryan, Prakhar and Aditya")
        speak("my name is eve.. i am a personal assistant.. my creator is mr.aarryan, Prakhar and Aditya")
    elif 'hello' in query:
        print("Heyy.. I am listening.. What Can I Do For You")
        speak("Heyy.. I am listening.. What Can I Do For You")
    elif 'take a screenshot' in query:
        speak("taking a screen shot")
        myScreenshot = pyautogui.screenshot()

        myScreenshot.save(f"C:\\Users\\Aryan\\OneDrive\\Pictures\\Screenshots\\ss.png")