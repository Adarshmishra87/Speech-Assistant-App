import speech_recognition as sr
r=sr.Recognizer()
import urllib.parse
import time
import webbrowser
import os
import playsound
import random
from gtts import gTTS
from time import ctime
from datetime import datetime

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            maria_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            maria_speak('Sorry, I did not get that')
        except sr.RequestError:
            maria_speak('Sorry, my speech service is down')
        return voice_data
    
def maria_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,1000000)
    audio_file='audio-' + str(r) + '.mp3'
    #tts is text to speech
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respones(voice_data):
    if 'what is your name' in voice_data:
        maria_speak('My name is Maria')
    if 'what time is it' in voice_data:
        maria_speak(ctime())
    if 'what date is it' in voice_data:
        maria_speak(f"Today’s date is {datetime.now().strftime('%Y-%m-%d')}")
    if 'search' in voice_data:
        search=record_audio('What do you want to search for?')
        url='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        maria_speak('Here is what I found for '+search)
    if 'find location' in voice_data:
        location=record_audio('What is the location?')
        encoded_location = urllib.parse.quote(location)
        url = f'https://www.google.com/maps/place/{encoded_location}/'
        webbrowser.get().open(url)
        maria_speak('Here is the location you searched for ' + location)
    
    if 'play the song' in voice_data:
        song=record_audio('What you want to play?')
        encoded_song = urllib.parse.quote(song)
        url = f'https://www.youtube.com/results?search_query={encoded_song}'  
        webbrowser.get().open(url)
        maria_speak(f'Here is the song you searched for: {song}')
    
    if 'exit' in voice_data:
        exit()

time.sleep(1)
maria_speak('How I can help you?')
while 1:
    voice_data=record_audio()
    respones(voice_data)