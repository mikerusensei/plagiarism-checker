import tkinter as tk
import datetime

from tkinter import PhotoImage
from checker import Checker
from functions import *

class GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.time = datetime.datetime.now()
        self.date = self.time.strftime('%A, %B %d, %Y')
        self.plagiarism_checker_window = None
        self.__configure_window()
        self.__add_frames()
        self.__add_labels()
        self.__add_logos()
        self.__add_buttons()

        configure_framepadding(self.header_frame, 20, 10)
        configure_framepadding(self.body_frame, 20, 10)
        configure_framepadding(self.logos_frame, 20, 10)
        configure_framepadding(self.headertext_frame, 20, 10)

        self.run_window()

    def __configure_window(self):
        self.title("Analysis of Algorithms")
        #self.state('zoomed')
        self.resizable(False, False)

    def __add_frames(self):
        self.frame = tk.Frame(self)
        self.frame.pack()

        self.main_frame = tk.LabelFrame(self.frame,)
        self.main_frame.grid(column=0, row=0)

        self.header_frame = tk.Frame(self.main_frame,)
        self.header_frame.grid(column=0, row=0)

        self.body_frame = tk.Frame(self.main_frame,)
        self.body_frame.grid(column=0, row=1,sticky="nsew")
        self.body_frame.grid_rowconfigure(0, weight=1)
        self.body_frame.grid_columnconfigure(0, weight=1)

        self.logos_frame = tk.Frame(self.header_frame,)
        self.logos_frame.grid(column=0, row=0)

        self.headertext_frame = tk.Frame(self.header_frame,)
        self.headertext_frame.grid(column=1, row=0)

    def __add_labels(self):
        lbl_welcome = tk.Label(self.headertext_frame, text="Practical Application", font=('Arial', get_window_fontsize(self), 'bold'))
        lbl_welcome.grid(column=0, row=0)

        lbl_time = tk.Label(self.headertext_frame, text=self.date, font=('Arial', get_window_fontsize(self), 'bold'))
        lbl_time.grid(column=0, row=1)

    def __add_logos(self):
        comics_logo = r"assets\comics_logo.png"
        productions_logo = r"assets\circle_logo.png"

        comics_img = PhotoImage(file=comics_logo)
        productions_img = PhotoImage(file=productions_logo)

        lbl_comics = tk.Label(self.logos_frame, image=comics_img)
        lbl_comics.grid(column=0, row=0)
        
        lbl_productions = tk.Label(self.logos_frame, image=productions_img)
        lbl_productions.grid(column=1, row=0)

        lbl_comics.image = comics_img
        lbl_productions.image = productions_img

    def __add_buttons(self):
        btn_checker = tk.Button(self.body_frame, text="Plagiarism Checker", command=self.command_plagiarism_window ,font=('Arial', get_window_fontsize(self), 'bold'))
        btn_checker.grid(column=0, row=0, sticky="ew")

        btn_exit = tk.Button(self.body_frame, text="Exit", command=self.command_exit ,font=('Arial', get_window_fontsize(self), 'bold'))
        btn_exit.grid(column=0, row=1, sticky="ew")

    def command_plagiarism_window(self):
        if not self.plagiarism_checker_window:
            self.plagiarism_checker_window = Checker(self, get_window_fontsize(self), self.date)
        
        self.iconify()
        self.plagiarism_checker_window.lift()

    def command_exit(self):
        self.destroy()

    def run_window(self):
        self.mainloop()