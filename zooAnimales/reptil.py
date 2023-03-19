from animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas, serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1 

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1 

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola