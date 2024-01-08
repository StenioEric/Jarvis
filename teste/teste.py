
import pyttsx3
engine = pyttsx3.init()
engine.say("Eu vou falar aqui papae")
engine.runAndWait()

voices = engine.getProperty('voices') 

for voice in voices:
    engine.getProperty(voice.id)