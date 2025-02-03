import speech_recognition as sr
import keyboard
import threading
import time

text_buffer = ""  # Stores transcribed text
running = True    # Flag to keep the loop running
last_backspace_time = 0  # To prevent rapid deletion

def recognize_speech():
    global text_buffer, running
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak... (Enter to save & quit, Backspace to delete last word)")

        while running:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)  # Increased timeout
                text = recognizer.recognize_google(audio)  # Google SpeechRecognition
                text_buffer += " " + text  # Append recognized text
              
                print("\r" + text_buffer.strip(), end="", flush=True)

            except sr.WaitTimeoutError:
                continue  # Keep listening if no speech detected
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError:
                print("\nAPI Connection corrupted!")
                running = False
                break

def keyboard_listener():
    global text_buffer, running, last_backspace_time

    while running:
        if keyboard.is_pressed("backspace") and text_buffer.strip():
            current_time = time.time()
            if current_time - last_backspace_time > 0.3:  # Prevents rapid deletions ( u can increase/decrease this )
                words = text_buffer.rstrip().split()  # Split into words
                if words:
                    words.pop()  # Remove last word
                    text_buffer = " ".join(words)  # Rejoin words
                print("\r" + text_buffer + " " * 10, end="", flush=True)  # Clear previous text
                last_backspace_time = current_time

        if keyboard.is_pressed("enter"):
            running = False  # Stop both threads
            with open("speech_output.txt", "w", encoding="utf-8") as f:
                f.write(text_buffer.strip())
            print("\nSaved to speech_output.txt. Exiting...")
            exit(0)  # Completely quit

speech_thread = threading.Thread(target=recognize_speech, daemon=True)
keyboard_thread = threading.Thread(target=keyboard_listener, daemon=True)

speech_thread.start()
keyboard_thread.start()

speech_thread.join()
keyboard_thread.join()
