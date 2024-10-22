import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk 


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly')
        self.title('StaminaPro')
        self.geometry('1400x600')

if __name__ == '__main__':
    app = App()
    app.mainloop()