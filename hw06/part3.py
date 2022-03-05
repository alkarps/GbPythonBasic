class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return f"{self.position}: {self.surname} {self.name}. Income: {self._income}"


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position = Position("Иван", "Батько", "Вышибало", 100, 1)
print(position)
print(position.name)
print(position.surname)
print(position.get_full_name())
print(position.position)
print(position._income)
print(position.get_total_income())
