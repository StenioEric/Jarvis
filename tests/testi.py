import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices') 
rate = engine.getProperty('rate')
voice_id = "brazil"
engine.setProperty('voice', voice_id)
engine.setProperty('rate', rate-80)

engine.say("SAFIRA MARIA É UMA MOLECA FOFINHA")
engine.runAndWait()