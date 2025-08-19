import av
import numpy as np
import wave
from streamlit_webrtc import AudioProcessorBase

class Recorder(AudioProcessorBase):
    def __init__(self):
        self.buffer = []

    async def recv_queued(self, frames):
        for frame in frames:
            audio = frame.to_ndarray()
            self.buffer.append(audio)
        return frames[-1] if frames else None  # Return last frame for compatibility

    def save_wav(self, filename):
        if not self.buffer:
            return False

        audio_data = np.concatenate(self.buffer, axis=0)
        sample_rate = 48000  # WebRTC default

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit audio
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.astype(np.int16).tobytes())

        return True