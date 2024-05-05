def get_window_fontsize(self):
    window_width = self.winfo_screenwidth()
    window_height = self.winfo_screenheight()

    font_size = min(window_width, window_height) // 40

    return font_size
    
def get_window_padding(self):
    window_width = self.winfo_screenmmwidth()
    window_height = self.winfo_screenmmheight()

    pad_x = int(window_width * 0.04)
    pad_y = int(window_height * 0.04)

    return pad_x, pad_y
    
def configure_widgetpadding(frame_name, function):
    pad_x, pad_y = function
    for widget in frame_name.winfo_children():
        widget.grid_configure(padx=pad_x, pady=pad_y)

def configure_widgetfont(frame_name, font_name, font_size):
    for widget in frame_name.winfo_children():
        widget.config(font=(font_name, font_size))

def configure_framepadding(frame_name, pad_x, pad_y):
    frame_name.grid_configure(padx=pad_x, pady=pad_y)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()