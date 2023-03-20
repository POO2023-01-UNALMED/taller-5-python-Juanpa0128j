class Zona():
    _animales = []

    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo

    @classmethod
    def agregarAnimales(cls, animal):
        cls._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo

    @classmethod
    def getAnimales(cls):
        return cls._animales
    
    @classmethod
    def setAnimales(cls, animales):
        cls._animales = animales