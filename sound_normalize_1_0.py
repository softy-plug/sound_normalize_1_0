import os

os.system("pip install sox")

import sox

import subprocess

# Get all audio files in the current directory
audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]

# Loop through the audio files and normalize them
for audio_file in audio_files:
    # Create a new file name for the normalized audio
    normalized_file = audio_file.replace('.wav', '_normalized.wav')

    # Normalize the audio using Sox
    subprocess.call(['sox', audio_file, normalized_file, 'norm'])

# softy_plug