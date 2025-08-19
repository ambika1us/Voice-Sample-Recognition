import numpy as np
import librosa
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Load model and encoder once
model = load_model("E:/Projects/PyCharm/Voice Sample Recognition/emotion_model.h5")
classes = np.load("E:/Projects/PyCharm/Voice Sample Recognition/classes.npy", allow_pickle=True)
le = LabelEncoder()
le.classes_ = classes

def predict_emotion(audio_path, n_mfcc=40):
    y, sr = librosa.load(audio_path, sr=None)
    if y is None or len(y) == 0:
        raise ValueError("Invalid or empty audio file.")
    y = (y - np.mean(y)) / np.std(y)  # normalize
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    features = np.mean(mfcc.T, axis=0).reshape(1, -1)

    probs = model.predict(features)[0]
    top_idx = np.argmax(probs)
    emotion = le.inverse_transform([top_idx])[0]
    confidence = probs[top_idx]
    return emotion, confidence, probs