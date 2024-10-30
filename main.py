import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.trainer import Trainer
from config.lessonss import all_lesonts
from module.analitic import AnaliticFrame

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly') #darkly
        self.title('StaminaPro')
        self.geometry('1500x900')

        self.all_lesonts = all_lesonts
        self.current_trainer = None  # Хранение текущего фрейма Trainer

        # Фрейм для загрузки виджетов
        self.widget_frame = tk.Frame()
        self.widget_frame.pack(expand=True, fill=tk.BOTH)

        #AnaliticFrame(self)
        
        self.create_menu()
        self.home()

    def create_menu(self):
        """Написал част GPT"""
        menu_bar = ttk.Menu(self)
        lessons_menu = ttk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Home', command=self.home)
        
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
        """Загрузка фрейма для тренировки"""
        self.clear_frame()
        self.current_trainer = Trainer( self.widget_frame, lesson_data)
        self.current_trainer.pack(expand=True)
    
    def home(self):
        """Загрузка фрейма аналитики, являеться домашней страницей"""
        self.clear_frame()
        self.homeframe = AnaliticFrame( self.widget_frame)

    def clear_frame(self):
        """Удаляет все виджеты из фрейма для загрузки."""
        for widget in self.widget_frame.winfo_children():
            widget.destroy()
        


if __name__ == '__main__':
    app = App()
    app.mainloop()