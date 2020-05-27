class FiguraGeometrica:

    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def __str__(self):
        # Solo le hacia falta los self a cada metodo
        return "Alto: " + str(self.get_alto()) + " Ancho: " + str(self.get_ancho())
