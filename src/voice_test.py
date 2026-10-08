"""Before/after sample of Japanese words in Sena's voice: output/voice_test.mp3 (no respelling, then respelled).

python src/voice_test.py
"""
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_episode as me  # noqa: E402

LINES = [
    "I ate an onigiri at my desk.",
    "Kato-san said, daijoubu.",
    "In Japan, we call it nemawashi.",
    "We say otsukaresama all day.",
    "Kuuki wo yomu. Reading the air.",
    "I'm Sena Sato, and this is Ryo and Kenta.",
]


def main():
    out = os.path.join(me.ROOT, "output")
    os.makedirs(out, exist_ok=True)
    parts = []
    gap = np.zeros(int(0.6 * me.SR), np.float32)
    for label, fn in (("Before.", lambda t: t), ("After.", me.spoken)):
        for text in [label] + LINES:
            mp3 = os.path.join(out, "vt.mp3")
            me._synth("SENA", fn(text) if text not in ("Before.", "After.") else text, mp3)
            parts += [me.decode(mp3), gap]
        parts.append(np.zeros(int(1.0 * me.SR), np.float32))
    pcm = np.concatenate(parts)
    wav = os.path.join(out, "voice_test.wav")
    import wave
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(me.SR)
        w.writeframes((np.clip(pcm, -1, 1) * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", wav, "-b:a", "128k", os.path.join(out, "voice_test.mp3")], check=True)
    print("output/voice_test.mp3")


if __name__ == "__main__":
    main()
