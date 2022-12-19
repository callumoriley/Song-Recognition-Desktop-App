# Song-Recognition-Desktop-App

A simple desktop app to recognize what song is playing on your computer by listening to the system audio. Only works on Windows machines

## Requirements
- ffmpeg (in PATH)
- [numpy](https://pypi.org/project/numpy/)
- [PythonLoopback](https://github.com/callumoriley/PythonLoopback)
- [shazam.py](https://pypi.org/project/shazam.py/)
- [pydub](https://pypi.org/project/pydub/)

## Acknowledgements

### I pulled code from a couple sources to make this work quickly. Here they are:
Turning a numpy array into an MP3 file:
https://stackoverflow.com/questions/66191480/how-to-convert-a-numpy-array-to-a-mp3-file
(originally from https://stackoverflow.com/questions/53633177/how-to-read-a-mp3-audio-file-into-a-numpy-array-save-a-numpy-array-to-mp3)

Interfacing with the Shazam API:
https://pypi.org/project/shazam.py/
