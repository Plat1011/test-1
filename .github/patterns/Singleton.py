class Logger:
    _logger = None

    def __new__(cls):
        if not cls._logger:
            cls._logger = super().__new__(cls)
            cls._logger.messages = []
        return cls._logger

    def add_message(self, text):
        self.messages.append(text)
        print(f"Лог добавлен: {text}")

    def show_log(self):
        return self.messages

logger1 = Logger()
logger1.add_message("Первое сообщение")

logger2 = Logger()
logger2.add_message("Второе сообщение")

print(f"Один и тот же логгер: {logger1 is logger2}")
print(f"Все сообщения: {logger1.show_log()}")