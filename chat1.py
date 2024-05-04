import openai
from gtts import gTTS
import pygame
from record1 import speech_text
import streamlit as st
import dotenv
import os


dotenv.load_dotenv()
KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = KEY


def play():

    text = speech_text()

    message = [{"role": "system", "content": "You are a useful assistant, which can understand the prompt and response without asking question"}]
    message.append(
        {'role': 'user', "content": f"{text}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=message,
                                            max_tokens=500,
                                            temperature=0)

    rep = response['choices'][0]['message']['content']

    # GTTS

    tts = gTTS(text=rep, lang='fr')
    tts.save("parole_generée.mp3")

    st.write('réponse...')
    # LECTURE

    pygame.mixer.init()

    pygame.mixer.music.load("parole_generée.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.quit()


def play_translate():
    text = speech_text()

    message = [{"role": "system", "content": "You will receive sentences in French and you must translate them correctly into English. the person has difficulty speaking French, guesses what he means from the key words, does not ask questions and just translates by guessing"}]
    message.append(
        {'role': 'user', "content": f"{text}"})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=message,
                                            max_tokens=500,
                                            temperature=0)

    rep = response['choices'][0]['message']['content']

    # GTTS

    tts = gTTS(text=rep, lang='en', slow=True)
    tts.save("parole_generée.mp3")

    st.write('réponse...')
    # LECTURE

    pygame.mixer.init()

    pygame.mixer.music.load("parole_generée.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.quit()
