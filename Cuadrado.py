from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.set_alto(self,lado)
        FiguraGeometrica.set_ancho(self,lado)
        Color.set_color(self,color)
        
    def area(self):
        return FiguraGeometrica.get_alto(self) * FiguraGeometrica.get_ancho(self)
    
    def __str__(self):
        return FiguraGeometrica.__str__(self)+"el area del cuadrado es: "+str(area())+" y es de "+Color.__str__(self)
        