from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass

    def common_fabric_consumption(self, others_clothes):
        result = self.fabric_consumption
        for clothes in others_clothes:
            result += clothes.fabric_consumption
        return result


class Coat(Clothes, ABC):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes, ABC):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


suit = Suit("Armani", 200)
print(suit.fabric_consumption)
print(Coat("Armani", 65).fabric_consumption)
print(Coat("Armani", 65).common_fabric_consumption([Suit("Armani", 200)]))
