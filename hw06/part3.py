class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        if type(income) == dict:
            self._income = income
        else:
            self._income = {"wage": 0, "bonus": 0}

    def __str__(self):
        return f"{self.position}: {self.surname} {self.name}. Income: {self._income}"


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] * 12 + self._income["bonus"]


def print_position(position):
    print(position)
    print(position.name)
    print(position.surname)
    print(position.get_full_name())
    print(position.position)
    print(position._income)
    print(position.get_total_income())


print_position(Position("Иван", "Батько", "Вышибало", {"wage": 100, "bonus": 1}))
print_position(Position("Иван", "Батько", "Вышибало", ()))
