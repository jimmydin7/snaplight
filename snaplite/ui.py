import tkinter as tk
from tkinter import ttk

class SnaplightUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snaplight")
        self.configure(bg="#23272a")
        self.resizable(False, False)
        self._setup_style()
        self._main_frame = tk.Frame(self, bg="#23272a")
        self._main_frame.pack(expand=True, fill='both')
        self._center_window(270, 180)
        self.show_main_menu()

    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Dark.TButton',
                        font=('Segoe UI', 11, 'bold'),
                        foreground='#f7f7f7',
                        background='#2c2f33',
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='#7289da',
                        padding=10)
        style.map('Dark.TButton',
                  background=[('active', '#7289da')])
        style.configure('Red.TButton',
                        font=('Segoe UI', 11, 'bold'),
                        foreground='#fff',
                        background='#e74c3c',
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='#c0392b',
                        padding=10)
        style.map('Red.TButton',
                  background=[('active', '#c0392b')])
        style.configure('Back.TButton',
                        font=('Segoe UI Symbol', 13),
                        foreground='#f7f7f7',
                        background='#23272a',
                        borderwidth=0,
                        padding=2)
        style.map('Back.TButton',
                  background=[('active', '#2c2f33')])

    def clear_frame(self):
        for widget in self._main_frame.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_frame()
        btn_capture = ttk.Button(self._main_frame, text="Capture Screenshot", style='Dark.TButton', command=self.show_capture_menu)
        btn_exit = ttk.Button(self._main_frame, text="Exit", style='Red.TButton', command=self.quit)
        btn_capture.pack(pady=(38, 14), padx=36, fill='x')
        btn_exit.pack(pady=(0, 28), padx=36, fill='x')

    def show_capture_menu(self):
        self.clear_frame()

        btn_back = ttk.Button(self._main_frame, text="\u2190", style='Back.TButton', command=self.show_main_menu)
        btn_back.place(x=10, y=10, width=28, height=28)

        center_frame = tk.Frame(self._main_frame, bg="#23272a")
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        btn_full = ttk.Button(center_frame, text="Fullscreen", style='Dark.TButton', command=lambda: self._capture('fullscreen'))
        btn_region = ttk.Button(center_frame, text="Select Region", style='Dark.TButton', command=lambda: self._capture('region'))
        btn_full.pack(pady=(0, 16), padx=20, fill='x')
        btn_region.pack(pady=(0, 0), padx=20, fill='x')

    def _center_window(self, width, height):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def _capture(self, mode):

        print(f"cp mode: {mode}")
        self.show_main_menu()

if __name__ == "__main__":
    app = SnaplightUI()
    app.mainloop()
