import pyttsx3   # for taking the voice 
import datetime # For noting the current time of our pc
import speech_recognition as sr  # For recognizing our speech and taking input from the microphone
import wikipedia # To do wikipedia searches (Basically task feature)
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): # The bot will wish as according to the current time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 
    speak("I am Jarvis sir , How may I help you")

def takeCommand():
    #This function takes input from the user via the microphone and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        # print(e) 
        print("Say That again please...")
        return "None"

    return query   




if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True: # This will be used for definig the tasks.
    # if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Openning Youtube")
            webbrowser.open("youtube.com")
        
        elif 'open goggle' in query:
            speak("Opennig Google")
            webbrowser.open("google.com")
        
        elif 'play anime' in query:
            speak("Openning Zoro")
            webbrowser.open("zoro.to")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Piyush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Openning VS code")
            os.startfile(codePath)

        elif 'open atom' in query:
            atom = 'C:\\Users\\Piyush\\AppData\\Local\\atom\\atom.exe'
            speak("Openning Atom")
            os.startfile(atom)
        
        elif 'open illustrator' in query:
            adobe = "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(adobe)

        # elif 'play valorant' in query:
        #     valo = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe" '--launch-product=valorant --launch-patchline=live'
        #     os.startfile(valo)

        # elif 'stop' in query:
        #      False

        

