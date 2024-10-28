import pygame

class Sound:
    active_events = set()  # Используем множество для уникальных событий

    def __init__(self, path_sound):
        self.path_sound = path_sound
        pygame.mixer.init()  # Инициализация модуля смешивания
        self.sound = pygame.mixer.Sound(path_sound)  # Загружаем звук

    def start_play(self, keysym):
        """Добавляем клавишу в список если ее нету и запускаем звук"""
        if keysym not in Sound.active_events:
            Sound.active_events.add(keysym)
            # Запускаем звук на новом канале, чтобы не прерывать предыдущий
            self.sound.play()  # Звук может накладываться

    def stop_play(self, keysym):
        """Удаляем клавишу из списка при отпускании"""
        if keysym in Sound.active_events:
            Sound.active_events.remove(keysym)

# Пример использования:
# Создаем экземпляр класса Sound для правильного звука
sound_correct = Sound("path_to_correct_sound.wav")
sound_incorrect = Sound("path_to_incorrect_sound.wav")

def on_key_press(e):
    """Обработка нажатия клавиши"""
    if e.keysym == "CorrectKey":  # Замените "CorrectKey" на нужную клавишу
        sound_correct.start_play(e.keysym)
    elif e.keysym == "IncorrectKey":  # Замените "IncorrectKey" на нужную клавишу
        sound_incorrect.start_play(e.keysym)

def on_key_release(e):
    """Обработка отпускания клавиши"""
    sound_correct.stop_play(e.keysym)
    sound_incorrect.stop_play(e.keysym)
