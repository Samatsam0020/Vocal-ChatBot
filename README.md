# 🎤 Vocal ChatBot

The **Vocal ChatBot** is an interactive voice-based chatbot application built using OpenAI's GPT, Whisper for speech recognition, and Streamlit for the user interface. This chatbot operates without memory, providing instant responses to voice inputs in both French and English.

## Features

- 🗣️ **Voice Interaction:** Communicate with the chatbot using voice commands.
- 🌍 **Translation Capability:** Translate spoken French sentences into English.
- 🤖 **OpenAI Integration:** Leverages OpenAI's GPT model for generating responses.
- 🎶 **Text-to-Speech:** Provides audio responses using Google Text-to-Speech (gTTS).

## Files

- **`app.py`:** Main Streamlit application for the user interface.
- **`chat1.py`:** Contains the logic for handling chatbot interactions and translations.
- **`record1.py`:** Manages audio recording and processing of speech input.
- **`requirements.txt`:** Lists the required Python packages for the project.
- **`.env`:** (To be created) Contains your OpenAI API key.
- **`.gitignore`:** Specifies files and directories to be ignored by Git.

## Requirements

Make sure you have Python installed. You can install the required packages using:

```bash
pip install -r requirements.txt

## Setup

    Create a .env file: In the root directory of the project, create a file named .env and add your OpenAI API key in the following format:
    OPENAI_API_KEY=your_api_key_here

## Getting Started

    Run the Application: Launch the Streamlit app by executing:

```bash
streamlit run app.py

Interact with the ChatBot:
Select "ChatBot" to start a conversation with the SAM ChatBot.
Choose "Traduction Français-Anglais" to translate spoken French sentences into English.

Voice Input: Click the "Commencer" button to start recording your voice input, and the bot will respond accordingly.

## Contact

📬 For any inquiries or feedback, feel free to reach out to me at [ssamat0020@gmail.com].

    🎤 ChatBot Mode: Speak to the chatbot and receive voice responses.
    🌐 Translation Mode: Speak in French, and the chatbot will translate and respond in English.
