📣 Emotion Recognition from Voice — Streamlit App
A lightweight, interactive web app for recognizing emotions from voice recordings using deep learning. Supports both audio file upload and live microphone input, with real-time predictions and confidence visualization.

🚀 Features
- 🎙️ Record or Upload Audio
Choose between live microphone input or uploading .wav files.
- 🤖 Emotion Prediction
Uses a trained CNN-GRU model to classify emotions like happy, sad, angry, etc.
- 📊 Confidence Visualization
Displays prediction probabilities as a horizontal bar chart using Altair.
- 🔊 Audio Playback
Listen to your input directly in the app.
- 📈 Modular & Reproducible
Built with clean modular code, config-driven training, and CLI support.




📦 Installation
git clone https://github.com/yourusername/emotion-voice-app.git
cd emotion-voice-app
pip install -r requirements.txt
streamlit run app.py



🧪 Usage
- Launch the app with streamlit run app.py
- Choose Upload or Record
- Submit your audio
- View predicted emotion and confidence chart

🛠️ Deployment
Deploy easily on Streamlit Cloud:
- Push this repo to GitHub
- Go to Streamlit Cloud → New App
- Select your repo and set app.py as the entry point
- Done!



🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

📜 License
MIT License. See LICENSE file for details.


