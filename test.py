import tkinter as tk
import winsound

import tkinter as tk
import winsound

class TypingTrainer(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.correct_sound = "sounds/click-button.wav"  # путь к звуку для правильной буквы
        self.incorrect_sound = "sounds/click-button.wav"  # путь к звуку для ошибки

        self.focus_set()  # Устанавливаем фокус на фрейм

        self.bind("<Key>", self.check_key)

    def play_sound(self, sound):
        winsound.PlaySound(sound, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def check_key(self, event):
        # Пример проверки на правильный ввод
        if event.char == 'а':  # допустим, правильный ввод — 'a'
            self.play_sound(self.correct_sound)
        else:
            self.play_sound(self.incorrect_sound)

root = tk.Tk()
root.geometry('500x500')
trainer = TypingTrainer(root)
trainer.pack()
root.mainloop()
