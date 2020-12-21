import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyjokes
from playsound import playsound


engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
    speak("I am friday sir... Please tell me... How May I Help you")
    print('Hi, how can I help?')


def takeComand():
    # it takes commaands through microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print('User said: ' +query)
            if 'friday' in query:
                query = query.replace('friday', '')

        except Exception as e:
            print(e)
            speak('Pardon Me, please say that again.')
            return "None"
        return query

if __name__ == "__main__":
    
    wishMe()
    # speak("But remember, Vanshu is a good boy and My creator")
    while True:
    # if 1:
        query = takeComand().lower()

        if 'stop' in query or 'good bye' in query or 'ok bye' in query or 'chup' in query or 'goodbye' in query:
            speak('Sure, I can do that')
            # exit()
            break

        elif 'tell me about' in query or 'wikipedia' in query or 'wiki' in query:   
            query = query.replace('wikipedia', '')
            query = query.replace('wiki', '')
            query = query.replace('tell me about', '')
            query = query.replace('search', '')
            person = query.replace('on', '')
            speak('Searching ' +person+ ' on Wikipedia...')
            results = wikipedia.summary(person, sentences=1)
            print(results)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Opening Youtube...')
            print('Opening YouTube...')

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak('Opening gmail...')
            print('Opening Gmail...')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('Opening Google...')
            print('Opening Google...')
        
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speak('Opening Stack overflow...')
            print('Opening Stack Overflow...')
        
        elif 'news' in query:
            webbrowser.open('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are the top news for you..')

        elif 'search' in query:
            query = query.replace('search', '')
            webbrowser.open_new_tab(query)
            speak('Here are some results..')

        elif 'play music' in query or 'play local music' in query:
            speak('Playing Music...')
            music_dir = 'C:\\Users\\ADMIN\\Desktop\\AI assistant\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            print('playing Music...')

        elif 'play random music' in query:
            speak('Playing Random Music...')
            music_dir = 'music\\'
            songs = os.listdir(music_dir)
            a = len(songs)
            num = random.randrange(0, a-1)
            print(num)
            os.startfile(os.path.join(music_dir, songs[num]))
            print('playing Random Music...')


        elif 'play' in query or 'on youtube' in query:
                query = query.replace('play', '')
                query = query.replace('youtube', '')
                query = query.replace('music', '')
                query = query.replace('on', '')
                song = query.replace('song', '')
                print('Playing...')
                speak('Playing ' + song + ' on Youtube')
                pywhatkit.playonyt(song)

        


        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%I : %M %p")
            print(Time)
            speak(f"Sir, the time is {Time}")
            
        elif 'open code' in query:
            speak('opening Visual Studio Code...')
            codePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            print('Opening Visual Studio Code..')

        elif 'set a reminder' in query:
            try:
                speak('what is the reminder?')
                content = takeComand()
                # speak(query)
                speak(f"Reminder saved..{content}")
            except:
                pass
            
        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)
            playsound('Laughing.mp3')

        
        # fun part
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Friday your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow, search wikipedia and google' 
                  'In different cities, get top headline news from times of india and you can ask me time and jokes too!')
        
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Aaditya")
            print("I was built by Aaditya")

        else:
            speak("I didn't get it. Please say that again...")