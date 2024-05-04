import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import streamlit as st


def speech_text():

    # Durée de l'enregistrement en secondes
    duree = 10

    # Fréquence d'échantillonnage
    frequence = 44100

    # Enregistrement du son
    enregistrement = sd.rec(int(duree * frequence),
                            samplerate=frequence, channels=1)
    sd.wait()

    # Sauvegarde du son dans un fichier WAV
    nom_fichier = "enregistrement.wav"
    write(nom_fichier, frequence, enregistrement)

    st.write('début traitement du son ...')
    model = whisper.load_model('base')
    result = model.transcribe(f'{nom_fichier}', fp16=False)
    st.write('finalisation ...')

    return result['text']
