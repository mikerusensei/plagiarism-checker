import tkinter as tk
import os

from tkinter import PhotoImage, filedialog, messagebox, ttk
from functions import *
from progressbar import Loading_Screen

class Checker(tk.Toplevel):
    def __init__(self, master=None, font_size=None, date=None):
        super().__init__(master)
        self.font_size = font_size
        self.date = date
        self.file_1_path = None
        self.file_2_path = None
        self.__configure_window()
        self.__add_frames()
        self.__add_logos()
        self.__add_buttons()
        self.__add_labels()

        configure_framepadding(self.header_frame, 20, 10)
        configure_framepadding(self.body_frame, 20, 10)
        configure_framepadding(self.logos_frame, 20, 10)
        configure_framepadding(self.headertext_frame, 20, 10)

    def __configure_window(self):
        self.title("Plagiarism Checker")
        # self.state('zoomed')
        self.resizable(False, False)

    def __add_frames(self):
        self.frame = tk.Frame(self)
        self.frame.pack()

        self.main_frame = tk.LabelFrame(self.frame,)
        self.main_frame.grid(column=0, row=0)

        self.header_frame = tk.Frame(self.main_frame,)
        self.header_frame.grid(column=0, row=0)

        self.body_frame = tk.LabelFrame(self.main_frame,)
        self.body_frame.grid(column=0, row=1, sticky="nsew")
        self.body_frame.grid_rowconfigure(0, weight=1)
        self.body_frame.grid_columnconfigure(0, weight=1)

        self.btn_frame = tk.Frame(self.main_frame,)
        self.btn_frame.grid(column=0, row=2,sticky="nsew")
        self.btn_frame.grid_rowconfigure(0, weight=1)
        self.btn_frame.grid_columnconfigure(0, weight=1)

        self.logos_frame = tk.Frame(self.header_frame,)
        self.logos_frame.grid(column=0, row=0)

        self.headertext_frame = tk.Frame(self.header_frame,)
        self.headertext_frame.grid(column=1, row=0)

    def __add_labels(self):
        lbl_welcome = tk.Label(self.headertext_frame, text="Plagiarism Checker", font=('Arial', self.font_size, 'bold'))
        lbl_welcome.grid(column=0, row=0)

        lbl_time = tk.Label(self.headertext_frame, text=self.date, font=('Arial', self.font_size, 'bold'))
        lbl_time.grid(column=0, row=1)

        self.lbl_file_1 = tk.Label(self.body_frame, text="File 1: ", font=('Arial', self.font_size, 'bold'))
        self.lbl_file_1.grid(column=0, row=0, sticky="w")

        self.lbl_file_2 = tk.Label(self.body_frame, text="File 2: ", font=('Arial', self.font_size, 'bold'))
        self.lbl_file_2.grid(column=0, row=1, sticky="w")

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
        btn_checker = tk.Button(self.btn_frame, text="Check", command=self.command_check ,font=('Arial', self.font_size, 'bold'))
        btn_checker.grid(column=0, row=0, sticky="ew")

        btn_return = tk.Button(self.btn_frame, text="Return", command=self.command_return ,font=('Arial', self.font_size, 'bold'))
        btn_return.grid(column=0, row=1, sticky="ew")

        btn_basis = tk.Button(self.body_frame, text="Select File", command=self.select_file_1, font=('Arial', self.font_size, 'bold'))
        btn_basis.grid(column=1, row=0, sticky="e")

        btn_del_basis = tk.Button(self.body_frame, text="Delete File", command=self.delete_file_1, font=('Arial', self.font_size, 'bold'))
        btn_del_basis.grid(column=2, row=0, sticky="e")

        btn_basis1 = tk.Button(self.body_frame, text="Select File", command=self.select_file_2, font=('Arial', self.font_size, 'bold'))
        btn_basis1.grid(column=1, row=1, sticky="e")

        btn_del_basis1 = tk.Button(self.body_frame, text="Delete File", command=self.delete_file_2, font=('Arial', self.font_size, 'bold'))
        btn_del_basis1.grid(column=2, row=1, sticky="e")

    def select_file_1(self):
        self.file_1_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_1_path:
            filename = os.path.basename(self.file_1_path)
            self.lbl_file_1.config(text="File 1: " + filename)

    def delete_file_1(self):
        self.file_1_path = None
        self.lbl_file_1.config(text="File 1:")

    def select_file_2(self):
        self.file_2_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_2_path:
            filename = os.path.basename(self.file_2_path)
            self.lbl_file_2.config(text="File 2: " + filename)

    def delete_file_2(self):
        self.file_2_path = None
        self.lbl_file_2.config(text="File 2:")

    def load_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
    
    def edit_distance(self, file_1_text, file_2_text):
        len1 = len(file_1_text)
        len2 = len(file_2_text)

        array = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        i = j = 0

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:
                    array[i][j] = j
                elif j == 0:
                    array[i][j] = i
                elif file_1_text[i - 1] == file_2_text[j - 1]:
                    array[i][j] = array[i - 1][j - 1]
                else:
                    array[i][j] = min(array[i][j - 1], array[i - 1][j], array[i - 1][j - 1]) + 1
        
        return array[i][j]
    
    def check_plagiarism(self, file_1_text, file_2_text):
        distance = self.edit_distance(file_1_text, file_2_text)
        max_len = max(len(file_1_text), len(file_2_text))

        score = (1 - (distance / max_len)) * 100

        return round(score, 2)
    
    def command_check(self):
        if self.file_1_path and self.file_2_path is not None:
            loading_screen = Loading_Screen()
            self.update()
            file_1_text = self.load_file(self.file_1_path)
            file_2_text = self.load_file(self.file_2_path)
            score = self.check_plagiarism(file_1_text, file_2_text)
            loading_screen.destroy()
            messagebox.showinfo("Plagiarism Check", f"Plagiarized Content: {score} %")
        else:
            messagebox.showwarning("File Selection", "Please select both files before checking plagiarism.")

    def command_return(self):
        self.master.deiconify()
        self.destroy()

    def destroy(self) -> None:
        super().destroy()
        if self.master:
            self.master.plagiarism_checker_window = None