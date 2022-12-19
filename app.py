import tkinter as tk
from recognize_audio import get_song_name_artist

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

    def getSong(self):
        song_name = get_song_name_artist(int(self.duration_entry.get()))
        self.output_field.config(text=song_name)