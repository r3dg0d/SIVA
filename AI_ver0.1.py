import pyttsx3
import speech_recognition as sr
import time
import random

sr.__version__ = '3.8.1'

greetings = ["Hello, world!", "I'm SIVA, an Intelligent, Kind, and helpful information assistant."]

def talk(text, lang="en-US", voice="en-US", sample_rate=16000, device="default"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voice)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    talk("Feel free to talk to your device.")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        talk("Sorry, I could not understand what you said. Please try again.")
    except sr.RequestError as e:
        talk("Sorry, could not process your request at the moment. Please try again later.")
        print(f"Error: {e}")
    return ""

# Commands for SIVA (Super Intelligent Voice assistant)
def run_siva():
    talk(random.choice(greetings))

    while True:
        text = recognize_speech().lower()
        if text == "power on":
            talk("Powering on.")
        elif text == "power off":
            talk("Powering off.")
        elif text == "what am i looking at":
            talk("Sorry, I cannot answer that question as I do not have access to your device's camera.")
        elif text == "what am i going to":
            talk("I am not sure. Could you please specify?")
        elif text == "play music":
            talk("Sorry, I do not have access to your device's music library.")
        elif text == "stop music":
            talk("Sorry, I do not have access to your device's music library.")
        elif text.startswith("search for"):
            query = text[10:]
            talk(f"Searching for {query}.")
        elif text == "convert video to 3d model":
            talk("Sorry, I do not have the necessary tools to perform this task.")
        elif text.startswith("video call"):
            args = text[11:].split()
            if len(args) != 2:
                talk("Sorry, could not recognize the name and location of the person you want to call.")
            else:
                name, location = args
                talk(f"Calling {name} at {location}.")
        elif text == "goodbye":
            talk("Goodbye! Have a nice day.")
            break
        else:
            talk("Sorry, I did not understand what you said. Please try again.")

if __name__ == "__main__":
    run_siva()

    # Google Bard AI branch
