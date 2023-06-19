class Figure:
    unit = "cm"

    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass
class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius
    def calculate_area(self):
        return 3.14159 * self._radius ** 2
def info(self):
    area = self.calculate_area()
    print(f"Circle radius: {self._radius}cm, area: {area}cm")
class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b
def calculate_area(self):
    return 0.5 * self._side_a * self._side_b
def info(self):
    area = self.calculate_area()
    area = self.calculate_area()
print(f"RightTriangle side a: {self._side_a}cm, side b: {self._side_b}cm, area: {area}cm")