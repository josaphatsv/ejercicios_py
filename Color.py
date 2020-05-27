class Color:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        # Solo le hacia falta el self
        return "Color: " + str(self.get_color())
