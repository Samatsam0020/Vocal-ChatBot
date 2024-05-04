import streamlit as st
from chat1 import play, play_translate


menu = ["ChatBot", "Traduction Français-Anglais"]
choice = st.sidebar.selectbox("", menu)

if choice == "ChatBot":
    st.title("SAM ChatBot")
    if st.button('Commencer'):
        play()

elif choice == "Traduction Français-Anglais":
    st.title("SAM traduction")
    if st.button('Commencer'):
        play_translate()
