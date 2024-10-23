import tkinter as tk
from tkinter import ttk

# Создаем главное окно
root = tk.Tk()
root.title("Виртуальная клавиатура")

# Поле ввода текста
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# Функция для обработки нажатий на кнопки клавиатуры
def on_button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

# Функция для удаления символа (Backspace)
def on_backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

# Функция для добавления пробела
def on_space():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + " ")

# Функция для очистки поля (Clear)
def on_clear():
    entry.delete(0, tk.END)

# Создание кнопок клавиатуры
buttons = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space', 'Backspace', 'Clear']
]

# Размещение кнопок на экране
for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == 'Space':
            button = ttk.Button(root, text=char, command=on_space)
            button.grid(row=i+1, column=j, columnspan=5, padx=5, pady=5, sticky="nsew")
        elif char == 'Backspace':
            button = ttk.Button(root, text=char, command=on_backspace)
            button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif char == 'Clear':
            button = ttk.Button(root, text=char, command=on_clear)
            button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        else:
            button = ttk.Button(root, text=char, command=lambda c=char: on_button_click(c))
            button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

# Настраиваем размеры колонок и строк для лучшей адаптивности
for i in range(10):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Запуск приложения
root.mainloop()
