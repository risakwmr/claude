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


VARIANTS = {
    "nemawashi": ["neh-mah-wah-shee", "nay-mah-wah-shee", "nemma washee", "neh mah wah shee", "nemawashee"],
    "otsukaresama": ["oh-tsoo-kah-reh-sah-mah", "oats-kah-reh-sah-mah", "ohts kah reh sah mah", "otskaray sahmah", "oh-tskah-reh-sah-mah"],
    "kuuki wo yomu": ["koo-kee oh yoh-moo", "kookee oh yohmoo", "koo kee, oh, yo moo", "cookie oh yoh-moo", "kookie oh yomoo"],
}


def variants():
    """For each word: say "Number one" ... then the word in a short sentence, so the best spelling can be picked."""
    out = os.path.join(me.ROOT, "output")
    os.makedirs(out, exist_ok=True)
    parts = []
    gap = np.zeros(int(0.5 * me.SR), np.float32)
    mp3 = os.path.join(out, "vt.mp3")
    for word, spells in VARIANTS.items():
        me._synth("SENA", f"{word}.", mp3)  # the word as written, for reference
        parts += [me.decode(mp3), gap, gap]
        for k, sp in enumerate(spells, 1):
            me._synth("SENA", f"Number {k}.", mp3)
            parts += [me.decode(mp3), gap]
            me._synth("SENA", f"In Japan, we call it {sp}.", mp3)
            parts += [me.decode(mp3), gap, gap]
        parts.append(np.zeros(int(1.2 * me.SR), np.float32))
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
    variants() if "--variants" in sys.argv or os.environ.get("VOICE_TEST") == "variants" else main()
