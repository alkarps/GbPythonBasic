from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes, ABC):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes, ABC):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def fabric_consumption(self):
        return self.height * 2 + 0.3


print(Suit("Armani", 200).fabric_consumption())
print(Coat("Armani", 65).fabric_consumption())