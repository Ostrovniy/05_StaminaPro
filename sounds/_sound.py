import winsound
import pygame

class SoundPygame:
    """Класс управляет звуком, start_play - запускает звук и сохраняет 
    активное событие, clear_event_list - очищает события, система от 
    спама когда зажали кнопку на клавитатуре и звук вызываеться очень
    много раз"""
    active_events = list()  

    def __init__(self, path_sound):
        self.path_sound = path_sound
        pygame.mixer.init()  # Инициализация модуля смешивания
        self.sound = pygame.mixer.Sound(path_sound)  # Загружаем звук

    def start_play(self, keysym):
        """Добавляем клавишу в список если ее нету и запускаем звук"""
        if keysym not in SoundPygame.active_events:
            SoundPygame.active_events.append(keysym)
            # Запускаем звук на новом канале, чтобы не прерывать предыдущий
            self.sound.play()  # Звук может накладываться

    @staticmethod
    def clear_event_list(keysym):
        """Удаляем клавишу из списка при отпускании"""
        if keysym in SoundPygame.active_events:
            SoundPygame.active_events.remove(keysym)



