class EuropeanSocket:
    def voltage(self):
        return 220

    def live(self):
        return "Фаза (220V)"

    def neutral(self):
        return "Нейтраль"

    def earth(self):
        return "Земля"


class USPlug:
    def voltage(self):
        return 110

    def hot(self):
        return "Фаза (110V)"

    def neutral(self):
        return "Нейтраль"


class USPlugAdapter:
    def __init__(self, us_plug):
        self.us_plug = us_plug

    def voltage(self):
        return self.us_plug.voltage()

    def live(self):
        return self.us_plug.hot()

    def neutral(self):
        return self.us_plug.neutral()

    def earth(self):
        return "Адаптер: без заземления"


european_socket = EuropeanSocket()
print("Европейская розетка:")
print(f"  Напряжение: {european_socket.voltage()}V")
print(f"  Контакты: {european_socket.live()}, {european_socket.neutral()}, {european_socket.earth()}")

us_plug = USPlug()
adapter = USPlugAdapter(us_plug)

print("\nАмериканская вилка через адаптер:")
print(f"  Напряжение: {adapter.voltage()}V")
print(f"  Контакты: {adapter.live()}, {adapter.neutral()}, {adapter.earth()}")