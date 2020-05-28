from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base,altura , color):
        FiguraGeometrica.set_alto(self, altura)
        FiguraGeometrica.set_ancho(self, base)
        Color.set_color(self, color)

    def area(self):
        return FiguraGeometrica.get_ancho(self) * FiguraGeometrica.get_alto(self)

    def __str__(self):
        
        return FiguraGeometrica.__str__(self) + ", el area del Rectangulo es: " + str(
            self.area()) + " y es de " + Color.__str__(self)
