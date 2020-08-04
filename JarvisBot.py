import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    print("I am Jarvis. How may I help you?")
    speak("I am Jarvis. How may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        if 1:
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
            speak('Opening Youtube...')
            webbrowser.open("https://www.youtube.com/?gl=IN")

        elif 'song' in query:
            speak('Playing the song...')
            query = query.replace("jarvis ", "")
            query = query.replace("search ", "")
            query = query.replace("for ", "")
            query = query.replace("the ", "")
            query = query.replace("song ", "")
            speak(query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            
        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open("https://www.google.co.in/")

        elif 'open stackoverflow' in query:
            speak('Opening Stackoverflow...')
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            speak('Playing a song...could you tell me the song name')
            query = query.replace("jarvis ", "")
            query = query.replace("search ", "")
            query = query.replace("for ", "")
            query = query.replace("the ", "")
            query = query.replace("song ", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "PASTE YOUR VSCODE.exe PATH HERE"
            os.startfile(codePath)

        elif 'email to someone' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "someoneyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
