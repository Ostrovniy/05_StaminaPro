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
        if keysym not in Sound.active_events:
            Sound.active_events.append(keysym)
            # Запускаем звук на новом канале, чтобы не прерывать предыдущий
            self.sound.play()  # Звук может накладываться

    @staticmethod
    def clear_event_list(keysym):
        """Удаляем клавишу из списка при отпускании"""
        if keysym in Sound.active_events:
            Sound.active_events.remove(keysym)

class Sound:
    """не используеться по причине прирывания звуков при запуска звука"""
    active_events = [] # Список кнопок которые нажали, но еще не отпустили клавишу
    # Статус плерера, игать музыку или нет
    status = True

    def __init__(self, path_sound):
        """Класс управления звуками нажатия на клавиши"""
        self.path_sound = path_sound

    def start_play(self, keysym):
        """Запустить звук и добавить клавишу список кнопок которые нажаты"""
        if not Sound.status:
            return
        if keysym not in Sound.active_events:
            Sound.active_events.append(keysym)
            winsound.PlaySound(self.path_sound, winsound.SND_FILENAME | winsound.SND_ASYNC)

    @staticmethod
    def clear_event_list(keysym):
        """Удаляем клавишу из списка при отпускании, метод зыпускаеться при событии когда
        пользователь отпустил кнопку которую нажал
        Для ситуации когда зажали кнопку определенную и вызываеться музыка много раз"""
        if not Sound.status:
            return
        if keysym in Sound.active_events:
            Sound.active_events.remove(keysym)
            # Остановка звука ненужна, так как не успевает отыграть до момента отжатия клавиши
            #winsound.PlaySound(None, winsound.SND_PURGE)



