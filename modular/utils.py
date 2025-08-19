import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

classes = np.load("classes.npy", allow_pickle=True)
le = LabelEncoder()
le.classes_ = classes

def display_results(emotion, probs):
    top_idx = np.argmax(probs)
    confidence = probs[top_idx]
    st.success(f"Predicted Emotion: **{emotion}** ({confidence:.2%} confidence)")

    df = pd.DataFrame({"Emotion": le.classes_, "Confidence": probs})
    df = df.sort_values(by="Confidence", ascending=False)
    st.bar_chart(df.set_index("Emotion"))
