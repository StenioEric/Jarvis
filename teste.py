
# import speech_recognition as sr


# #Cria um reconhecedor 
# r = sr.Recognizer()

# #Abrir o microfone para captura
# with sr.Microphone() as source:

#     while True:

#         audio = r.listen(source) #Define microfone como fonte de áudio

#         print(r.recognize_google(audio, language ='pt'))

import pyttsx3

engine = pyttsx3.init()

# Obtém todas as vozes disponíveis
voices = engine.getProperty('voices')

# Exibe informações sobre cada voz
for voice in voices:
    print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

# Escolha o ID da voz desejada
voice_id = "seu_id_de_voz_aqui"

# Configura o mecanismo para usar a voz escolhida
engine.setProperty('voice', voice_id)

# Executa a síntese de fala
engine.say("Exemplo de texto em português")
engine.runAndWait()
