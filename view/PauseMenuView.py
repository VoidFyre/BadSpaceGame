import tkinter as tk
import pygame

class PauseMenuView(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.create_widgets()
        self.root = tk.Tk()

    def create_widgets(self):
        self.title = tk.Label(self, text="Paused", font=("Arial", 16))
        self.title.pack(pady=10)

        self.resume_button = tk.Button(self, text="Resume", command=self.resume)
        self.resume_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=5)

    def resume(self):
        self.master.destroy()

    def quit(self):
        self.master.destroy()
        pygame.quit()