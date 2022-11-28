import pytts
import speech_recognition as sr
import time
import random

sr.__version__ = '3.8.1'

print("Hello, world!") # print
print("I'm SIVA, an Intelligent, Kind, and helpful information assistant.")
print("loading code... please wait...")

def talk(recognizer, microphone):
    text,
    lang="en-US",
    voice="en-US",
    sample_rate=16000,
    device="cuda"
    ):
    """
    Talks the given text to the given language.

    Args:
        text (str): The text to be spoken.
        lang (str, optional): The language to use. Defaults to "en-US".
        voice (str, optional): The voice to use. Defaults to "en-US".
        sample_rate (int, optional): The sample rate to use. Defaults to 16000.
        device (str, optional): The device to use. Defaults to "cuda".
)

def speak(text, lang, voice = "en-US", sample_rate=16000, device="speaker"):
    """

    r = sr.Recognizer
    r.recognize_google("SIVA")
    r.add_word_list(lang, voice)
    SIVA = sr.AudioFile("Path to .wav audio file", sample_rate=sample_rate)
    print("Feel free to talk to your device.")
    with siva as source:
        audio = r.record(source)

        type(audio)

        r.recognize_google(audio)
    
    # Commands for SIVA (Super Intelligent Voice assistant)
    r.recognize_google(cmd1)

    #SIVA Home Commands
    cmd1 = 'Siva, Power on.'
    cmd2 = 'Siva, Power off.'
    cmd3 = 'Siva, What am I looking at?'
    cmd4 = 'Siva, What am I going to?'
    cmd5 = 'Siva, Play music.'
    cmd6 = 'Siva, Stop music.'
    cmd7 = ''
    r.recognize_google(cmd1)
    r.listen()
    r.recognize_google(cmd2)
    r.listen()
    r.recognize_google(cmd3)
    r.listen()
    r.recognize_google(cmd4)
    r.listen()
    r.recognize_google(cmd5)
    r.listen()
    r.recognize_google(cmd6)
    r.listen()
    

    print("Some commands you can ask me include music, power on, power off, and more.")
def input(text, lang, voice = "en-US", sample_rate  =16000, device  = "speaker"):
    input