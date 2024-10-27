import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.trainer import Trainer
from config.lessonss import all_lesonts

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly') #darkly
        self.title('StaminaPro')
        self.geometry('1500x900')

        self.all_lesonts = all_lesonts
        self.current_trainer = None  # Хранение текущего фрейма Trainer
        
        self.create_menu()

    def create_menu(self):
        """Написал част GPT"""
        menu_bar = ttk.Menu(self)
        lessons_menu = ttk.Menu(menu_bar, tearoff=0)
        
        # Рекурсивное добавление категорий и уроков
        self.add_menu_item(lessons_menu, self.all_lesonts)
        
        # Добавляем основную кнопку "Уроки" на панель меню
        menu_bar.add_cascade(label="Уроки", menu=lessons_menu)
        self.config(menu=menu_bar)

    def add_menu_item(self, parent_menu, items):
        """Написал част GPT"""
        for key, value in items.items():
            if isinstance(value, dict) and 'title' not in value:
                submenu = ttk.Menu(parent_menu, tearoff=0)
                parent_menu.add_cascade(label=key, menu=submenu)
                self.add_menu_item(submenu, value)
            else:
                parent_menu.add_command(label=value['title'], command=lambda v=value: self.show_trainer(v))
    
    def show_trainer(self, lesson_data):
        """Написал част GPT"""
        # Удаление текущего фрейма Trainer, если он есть
        if self.current_trainer is not None:
            self.current_trainer.destroy()
        
        # Создание нового фрейма Trainer с передачей данных урока
        self.current_trainer = Trainer(self, lesson_data)
        self.current_trainer.pack(expand=True)
        


if __name__ == '__main__':
    app = App()
    app.mainloop()