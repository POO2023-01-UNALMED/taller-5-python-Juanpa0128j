from animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas, salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1 

    @classmethod
    def crearSalamandras(cls, nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1 

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
