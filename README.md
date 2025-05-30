[![Made in Iran](https://img.shields.io/badge/made_in-iran-ffd700.svg?labelColor=0057b7)](https://github.com/RealUnfazed)
[![Build](https://img.shields.io/github/actions/workflow/status/RealUnfazed/PySTT/main.yml?branch=master)](#)
[![Release](https://img.shields.io/github/release/RealUnfazed/PySTT.svg)](#)
[![Downloads](https://img.shields.io/github/downloads/RealUnfazed/PySTT/total.svg)](#)
[![Discord](https://img.shields.io/discord/796410664460877865?label=discord)](https://discord.gg/tUa4V9S3MF)
[![Donate](https://img.shields.io/badge/donate-$$$-8a2be2.svg)](#)
[![Alireza Plus](https://img.shields.io/badge/Alireza-Plus-e4181c.svg?labelColor=0000ff)](#)

# PySTT (PySpeechToText)

PySTT is an offline and online real-time speech-to-text tool supporting both **Vosk** (offline) and **Google Speech Recognition** (online) engines.  
It transcribes spoken words seamlessly with live keyboard control to delete or save transcriptions.

# Changelog  
~~v1.0.0~~

# Known Issues  
~~⚠ No major issues detected yet~~

# ToDo List  

# Installation and Usage

First, make sure you have Python installed. Then install dependencies by running:

    pip install -r requirements.txt

If you're going to use "Offline" you need to download the Vosk offline model (e.g. [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models)) and extract it.  
Place the model folder in the same directory as the script or update the `MODEL_PATH` in the script accordingly.

Run the script with:

    py main.py


### Controls:
- **Speak** to transcribe text live.
- **Backspace** to delete the last spoken word.
- **Enter** to save the transcription to `speech_output.txt` and exit.

**Tested On Python 3.10+**

---

If you want help with setting up or customizing the tool, join the [Discord server](https://discord.gg/tUa4V9S3MF).

---

**License:** CC BY-NC-ND  
All my projects and repositories are licensed under this license.
