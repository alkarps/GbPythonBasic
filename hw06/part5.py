class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Запуск отрисовки")

    def __str__(self):
        return f"{type(self)}; title = {self._title}"


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print(f"{self._title} рисует синим")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        super().draw()
        print(f"{self._title} рисует серым и это можно стереть")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print(f"{self._title} выделяет текст")


def print_stationery(stationary):
    print(stationary)
    stationary.draw()


print_stationery(Stationery("Кисть"))
print_stationery(Pen())
print_stationery(Pencil())
print_stationery(Handle())
