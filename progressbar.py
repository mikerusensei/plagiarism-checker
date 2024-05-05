import tkinter as tk

class Loading_Screen(tk.Toplevel):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.__configure_window()
        self.__add_labels()

    def __configure_window(self):
        self.title("Loading...")
        self.geometry("200x200")

    def __add_labels(self):
        lbl_loading = tk.Label(self, text='Checking Plagiarism...')
        lbl_loading.pack()
