from PythonLoopback import record_buffer
import numpy as np
import pydub
from shazam import Shazam
import os

TIME_TO_RECORD = 10 # in seconds

# code heist from here: https://stackoverflow.com/questions/66191480/how-to-convert-a-numpy-array-to-a-mp3-file
def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")

def get_song_name_artist(record_time):
    audio_buffer = record_buffer(record_time)
    write("sound.mp3", 44100/2, audio_buffer)
    mp3_file = open("sound.mp3", "rb").read() # using code from here: https://pypi.org/project/shazam.py/

    with Shazam(mp3_file) as shazam:
        song_name = shazam.result["track"]["title"] + " by " + shazam.result["track"]["subtitle"]
    
    os.remove("sound.mp3")
    return song_name

if __name__ == "__main__":
    print(get_song_name_artist(TIME_TO_RECORD))
