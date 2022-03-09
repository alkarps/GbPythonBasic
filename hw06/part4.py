class Car:
    def __init__(self, color, name, is_police, speed=0):
        self.speed, self.color, self.name, self.is_police = speed, color, name, False
        if type(is_police) == bool:
            self.is_police = is_police

    def __str__(self):
        return f"""{type(self)} with params:
        name = {self.name}
        color = {self.color}
        speed = {self.speed}
        is_police = {self.is_police}"""

    def show_speed(self):
        self._show_speed_with_limits()

    def _show_speed_with_limits(self, limits=-1):
        if limits != -1 and self.speed > limits:
            print(f"Текущая скорость: {self.speed}! Внимание, скорость превышает максимально допустимую - 60 км в час")
        else:
            print(f"Текущая скорость: {self.speed} км в час!")

    def go(self):
        print(f"{self.name} поехала!")

    def stop(self):
        print(f"{self.name} остановилась!")

    def turn(self, direction):
        print(f"{self.name} повернулась в сторону {direction}!")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(color, name, False)

    def show_speed(self):
        super()._show_speed_with_limits(60)


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(color, name, False)

    def show_speed(self):
        super()._show_speed_with_limits(40)


class PoliceCar(Car):
    def __init__(self, name):
        super().__init__("Black and white", name, True)


def print_car(car):
    print(car)
    car.go()
    car.show_speed()
    car.speed = 50
    car.turn("left")
    car.show_speed()
    car.speed = 500
    car.turn("right")
    car.show_speed()
    car.stop()


print_car(TownCar("Lada", "Green"))
print_car(SportCar("Lamborghini", "Pink"))
print_car(WorkCar("Kamaz", "Yellow"))
print_car(PoliceCar("BMW"))
