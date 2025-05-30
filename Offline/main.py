import keyboard
import threading
import time
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import sys

# Config
MODEL_PATH = "vosk-model-small-en-us-0.15"  # Don't forget to download your model and place it inside the project folder — I haven't included it in this repository.
SAMPLE_RATE = 16000

# Globals
text_buffer = ""
running = True
last_backspace_time = 0
q = queue.Queue()

# Load model
try:
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)
except Exception as e:
    print("Model not found or failed to load:", e)
    sys.exit(1)

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def recognize_speech():
    global text_buffer, running

    print("Speak... (Enter to save & quit, Backspace to delete last word)")

    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while running:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                if result.get("text"):
                    text_buffer += " " + result["text"]
                    print("\r" + text_buffer.strip() + " " * 10, end="", flush=True)

def keyboard_listener():
    global text_buffer, running, last_backspace_time

    while running:
        if keyboard.is_pressed("backspace") and text_buffer.strip():
            current_time = time.time()
            if current_time - last_backspace_time > 0.3:
                words = text_buffer.rstrip().split()
                if words:
                    words.pop()
                    text_buffer = " ".join(words)
                print("\r" + text_buffer + " " * 10, end="", flush=True)
                last_backspace_time = current_time

        if keyboard.is_pressed("enter"):
            running = False
            with open("speech_output.txt", "w", encoding="utf-8") as f:
                f.write(text_buffer.strip())
            print("\nSaved to speech_output.txt. Exiting...")
            exit(0)

speech_thread = threading.Thread(target=recognize_speech, daemon=True)
keyboard_thread = threading.Thread(target=keyboard_listener, daemon=True)

speech_thread.start()
keyboard_thread.start()

speech_thread.join()
keyboard_thread.join()
