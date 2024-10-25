import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.trainer import Trainer

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly') #darkly
        self.title('StaminaPro')
        self.geometry('1400x600')

        #Trainer(self).pack(expand=True, fill=tk.BOTH)
        Trainer(self).pack(expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()