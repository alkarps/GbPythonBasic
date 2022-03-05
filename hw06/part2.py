class Road:

    def __init__(self, length, width):
        self.length, self.width = length, width

    def get_weight(self, weight, height):
        return self.length * self.width * weight * height


print(Road(20, 5000).get_weight(25, 5))
