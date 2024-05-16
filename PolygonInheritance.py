class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height


class Squer(Polygon):
    pass


my_traingle = Triangle(5, 4, "Blue")
print(my_traingle.num_sides)
