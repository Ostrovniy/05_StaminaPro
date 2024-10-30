import json

class Analytic:
    def __init__(self, leng):
        self.file_path = "analytics/db.json"
        self.leng = leng
        self.data = {}
        self.load_data()

    def gl_increment_quantity_true(self):
        """Увеличить количество введенных символов правильно на 1"""
        if self.leng == 'RU':
            self.data["global_ru"]["quantity_true"] += 1
        if self.leng == 'EN':
            self.data["global_en"]["quantity_true"] += 1

    def gl_increment_quantity_false(self):
        """Увеличить количество введенных символов не правельных на 1"""
        if self.leng == 'RU':
            self.data["global_ru"]["quantity_false"] += 1
        if self.leng == 'EN':
            self.data["global_en"]["quantity_false"] += 1

    def gl_increment_minutes_spent(self, value):
        """Увеличить количество минут печати"""
        if self.leng == 'RU':
            self.data["global_ru"]["minutes_spent"] += value
        if self.leng == 'EN':
            self.data["global_en"]["minutes_spent"] += value

    def gl_set_max_speed_record(self, value):
        """Увеличить количество минут печати"""
        if self.leng == 'RU':
            self.data["global_ru"]["print_speed_record"] = max(value, self.data["global_en"]["print_speed_record"])
        if self.leng == 'EN':
            self.data["global_en"]["print_speed_record"] = max(value, self.data["global_en"]["print_speed_record"])

    def gl_get_print_speed_record(self):
        """Получить текущи рекорд скорости печати"""
        if self.leng == 'RU':
            return self.data["global_ru"]["print_speed_record"]
        if self.leng == 'EN':
            return self.data["global_en"]["print_speed_record"]
        
    def gl_get_quantity_true(self):
        """Получить количество напечатаных символов"""
        if self.leng == 'RU':
            return self.data["global_ru"]["quantity_true"]
        if self.leng == 'EN':
            return self.data["global_en"]["quantity_true"]
        
    def gl_get_quantity_false(self):
        """Получить количество напечатаных символов c ошибками"""
        if self.leng == 'RU':
            return self.data["global_ru"]["quantity_false"]
        if self.leng == 'EN':
            return self.data["global_en"]["quantity_false"]
        
    def gl_get_minutes_spent(self):
        """Получить количество потречаного времени в минутах"""
        if self.leng == 'RU':
            return self.data["global_ru"]["minutes_spent"]
        if self.leng == 'EN':
            return self.data["global_en"]["minutes_spent"]
    
    def get_global(self):
        """Получить глобальную аналитику относительно языка"""
        config = {
            'RU': self.data['global_ru'],
            'EN': self.data['global_en'],
        }
        return config[self.leng]
    
    def load_data(self):
        """Загружает данные из JSON-файла и сохраняет их в переменной. self.data"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON.")

    def save_data(self):
        """Сохраняет текущие данные self.data в JSON-файл."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print("Ошибка при сохранении данных:", e)

