import streamlit as st
from input_handler import get_audio_input
from predict import predict_emotion
from utils import display_results

st.title("🎙️ Emotion Recognition from Voice")

audio_path = get_audio_input()

if audio_path:
    try:
        emotion, confidence, probs = predict_emotion(audio_path)
        display_results(emotion, probs)
    except Exception as e:
        st.error(f"Prediction failed: {e}")