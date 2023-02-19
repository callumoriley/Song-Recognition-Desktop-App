import tkinter as tk
from recognize_audio import get_song_name_artist

SAVE_FILE_NAME = __file__[:__file__.rfind("\\")]+"\\savedsongs.txt"

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Song Recognizer")
        self.minsize(200, 100)

        self.duration_entry = tk.Entry(self, text="Listening duration")
        self.duration_entry.insert(0, "10")
        self.duration_entry.pack()

        self.start_button = tk.Button(self, text="Recognize song!", command=self.getSong)
        self.start_button.pack()

        self.output_field = tk.Label(self, text="No song recognized")
        self.output_field.pack()

        self.save_button = tk.Button(self, text="Save recognized song", command=self.saveSong)
        self.save_button.pack()

    def getSong(self):
        try:
            self.song_name = get_song_name_artist(int(self.duration_entry.get()))
            self.output_field.config(text=self.song_name)
        except KeyError:
            print("Song not recognized")
            self.output_field.config(text="No song recognized")

    def saveSong(self):
        with open(SAVE_FILE_NAME, "a") as f:
            try:
                f.write(self.song_name+"\n")
                print("Song written to file")
            except AttributeError:
                print("Capture a song first")
