class Road:
    __weight = 25
    __height = 5

    def __init__(self, length, width):
        self.length, self.width = length, width

    def get_weight(self):
        return self.length * self.width * self.__weight * self.__height


print(Road(20, 5000).get_weight())
