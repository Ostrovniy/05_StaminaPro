import tkinter as tk
from tkinter import Menu, ttk

all_lesonts = {
    'Уроки от Валерия дернова': {
        "Уроки ао_ёъ": {
            'аовл':{
                'title': "аовл",
                "language": "РУ",
                "text": "ао оо ао оо ао оо оо оо ао оо ао оа ао оо оо оо"
            },
            'ыд':{
                'title': "ыд",
                "language": "РУ",
                "text": "оы да ыл вд ыв лд ыв од аы дв ыл"
            },
        },
        "Уроки АО_ЁЪ": {
            'АО':{
                'title': "АО",
                "language": "РУ",
                "text": "Ап Ор Ас От Ау Оф Ах Оц Ач Ош Ащ Оъ"
            }
        }
    },
    "БАЗОВЫЕ УРОКИ":{
        "ва ол":{
            'title': "ва ол",
            "language": "ру",
            "text": "аааооо ааоао оааоо аоаоа ооаоа ао оао"
        },
        "фы дж":{
            'title': "фы  дж",
            "language": "ру",
            "text": "ыыыддд ыыдыд дыыдд ыдыды"
        }
    }
}

class Trainer(ttk.Frame):
    def __init__(self, parent, lesson_data):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        # Отображение информации об уроке
        title = lesson_data.get('title', 'Без названия')
        language = lesson_data.get('language', 'Неизвестно')
        text = lesson_data.get('text', 'Текст не найден')
        
        ttk.Label(self, text=f"Заголовок: {title}", font=("Arial", 14, "bold")).pack(pady=5)
        ttk.Label(self, text=f"Язык: {language}", font=("Arial", 10)).pack(pady=5)
        ttk.Label(self, text=f"Текст урока:", font=("Arial", 10, "italic")).pack(pady=5)
        ttk.Label(self, text=text, wraplength=400, font=("Arial", 10)).pack(pady=5)

class MenuApp:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("Динамическое меню")
        self.current_trainer = None  # Хранение текущего фрейма Trainer
        
        self.create_menu()
        
    def create_menu(self):
        menu_bar = Menu(self.root)
        lessons_menu = Menu(menu_bar, tearoff=0)
        
        # Рекурсивное добавление категорий и уроков
        self.add_menu_item(lessons_menu, self.config)
        
        # Добавляем основную кнопку "Уроки" на панель меню
        menu_bar.add_cascade(label="Уроки", menu=lessons_menu)
        self.root.config(menu=menu_bar)
        
    def add_menu_item(self, parent_menu, items):
        for key, value in items.items():
            if isinstance(value, dict) and 'title' not in value:
                submenu = Menu(parent_menu, tearoff=0)
                parent_menu.add_cascade(label=key, menu=submenu)
                self.add_menu_item(submenu, value)
            else:
                parent_menu.add_command(label=value['title'], command=lambda v=value: self.show_trainer(v))
                
    def show_trainer(self, lesson_data):
        # Удаление текущего фрейма Trainer, если он есть
        if self.current_trainer is not None:
            self.current_trainer.destroy()
        
        # Создание нового фрейма Trainer с передачей данных урока
        self.current_trainer = Trainer(self.root, lesson_data)
        self.current_trainer.pack(fill="both", expand=True)

# Пример использования
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root, all_lesonts)
    root.mainloop()
