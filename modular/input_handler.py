import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from recorder import Recorder
from predict import predict_emotion
import altair as alt
import pandas as pd

def show_emotion_chart(probabilities, labels):
    df = pd.DataFrame({
        "Emotion": labels,
        "Confidence": probabilities
    })

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Confidence:Q", scale=alt.Scale(domain=[0, 1])),
        y=alt.Y("Emotion:N", sort="-x"),
        color=alt.Color("Emotion:N", legend=None),
        tooltip=["Emotion", "Confidence"]
    ).properties(
        width=500,
        height=300,
        title="Emotion Confidence Scores"
    )

    st.altair_chart(chart, use_container_width=True)


def get_audio_input():
    method = st.radio("Choose input method:", ["Upload", "Record"])

    if method == "Upload":
        file = st.file_uploader("Upload .wav file", type=["wav"])
        if file:
            path = "temp.wav"
            with open(path, "wb") as f:
                f.write(file.read())
            st.audio(path)
            return path

    elif method == "Record":
        webrtc_ctx = webrtc_streamer(
            key="audio-recorder",
            mode=WebRtcMode.SENDONLY,  # Only sending audio from mic to server
            audio_processor_factory=Recorder,
            media_stream_constraints={"audio": True, "video": False},
        )

        if webrtc_ctx and webrtc_ctx.audio_processor:
            if st.button("Save Recording"):
                success = webrtc_ctx.audio_processor.save_wav("output.wav")
                if success:
                    st.success("Recording saved as output.wav")
                    prediction = predict_emotion("output.wav")
                    labels = ["neutral", "happy", "sad", "angry", "fearful", "disgust"]
                    show_emotion_chart(prediction[2], labels)


                else:
                    st.warning("No audio recorded yet!")

    return None