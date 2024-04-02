class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


rectangle = Rectangle(5, 4)
print("Довжина Прямокутника:", rectangle.length)
print("Ширина Прямокутника:", rectangle.width)
print("Площа Прямокутника:", rectangle.area())
print("Периметр Прямокутника:", rectangle.perimeter())
