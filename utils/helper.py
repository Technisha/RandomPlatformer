from raylib.pyray import PyRay

pyray = PyRay()


class Vector2:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __call__(self):
        return pyray.Vector2(self.x, self.y)

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'

    def __str__(self):
        return f'X:{self.x}, Y:{self.y}'

    '''
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    '''

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector2(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector2(self.x % other.x, self.y % other.y)


class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x, self.y = x, y
        self.width, self.height = width, height

    def __call__(self):
        return pyray.Rectangle(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}, Width: {self.width}, Height: {self.height}'

    '''
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.width < other.width and self.height < other.height

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.width <= other.width and self.height <= other.height

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.width != other.width and self.height != other.height

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.width > other.width and self.height > other.height

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.width >= other.width and self.height >= other.height
    '''

    def __add__(self, other):
        return Rectangle(self.x + other.x, self.y + other.y, self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(self.x - other.x, self.y - other.y, self.width - other.width, self.height - other.height)

    def __mul__(self, other):
        return Rectangle(self.x * other.x, self.y * other.y, self.width * other.width, self.height * other.height)

    def __truediv__(self, other):
        return Rectangle(self.x / other.x, self.y / other.y, self.width / other.width, self.height / other.height)

    def __floordiv__(self, other):
        return Rectangle(self.x // other.x, self.y // other.y, self.width // other.width, self.height // other.height)

    def __mod__(self, other):
        return Rectangle(self.x % other.x, self.y % other.y, self.width % other.width, self.height % other.height)


class Screen:
    width = 800
    height = 450


class Fps:
    enabled = None
    cap = 60
