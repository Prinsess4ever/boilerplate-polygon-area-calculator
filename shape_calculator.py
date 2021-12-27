class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        result = ""
        for i in range(self.height):
            result += '*' * self.width + '\n'
        return result

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_amount_inside(self, other):
        result = self.width / other.width
        lol = self.height / other.height
        return int(result * lol)

    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side_lengte):
        self.width = side_lengte
        self.height = side_lengte

    set_width = set_side
    set_height = set_side

    def __repr__(self):
        return "Square(side=" + str(self.height) + ")"