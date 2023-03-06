import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import random
import webbrowser
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


greetings = ["hello", "hi", "what's up"]
byes = ["take care", "see you later", "good bye"]
greet = random.choice(greetings)
bye = random.choice(byes)

# this function is chatGPT's doing



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("what do you want today!")


def speak(text):
    """this function is responsible for speaking"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def listener():
    """this function is to take input from Mic"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        user_query = r.recognize_google(audio)
        print(f"user said: {user_query}\n")
    except Exception as e:
        # print(e)
        print("say again!")
        err = "no internet connection!"
        return err
    return user_query


def run_assistant():
    """this is the actually dealing with all user user_query!"""
    user_query = listener().lower()
    if user_query is None:
        return
    elif 'play' in user_query:
        query = user_query.replace('play', '')
        query = query.strip()
        if 'spotify' in user_query:
            try:
                play_on_spotify(query)
            except:
                pass
        else:
            play_music(query)
    elif 'who is' in user_query:
        query = user_query.replace("who is", "")
        query = query.strip()
        wiki_summary(query)
    elif 'what is' in user_query:
        query = user_query.replace('what is', "")
        wiki_summary(query)
    elif 'shutdown' in user_query:
        os.system('shutdown /s /t 1')
    
    elif 'search' in user_query:
        query = user_query.replace('search',"")
        webbrowser.open_new_tab(query)
    elif 'bye' in user_query or 'stop' in user_query:
        return "bye"
    else:
        generate_response(user_query)
        

def wiki_summary(find):
    result = wikipedia.summary(find, sentences=3)
    speak(result)


def play_music(song):
    speak(f"playing {song} on youtube.")
    pywhatkit.playonyt(song)


def play_on_spotify(song):
    client_id = '78ce57467f2540baa5eb256f86f62326'
    client_secret = '6de3840181144d7cad62fd68395efb2d'
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(song, limit=1)
    if result['tracks']['items']:
        track_uri = result['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        speak(f"Playing {song} on Spotify.")
    else:
        speak("Sorry, I could not find the song on Spotify.")


if __name__ == "__main__":
    wish()
    while (True):
        running = run_assistant()
        if  running == "bye":
            speak(bye+"have a good day!")
            break;
