class Película:
    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f'El nombre de la película es {self._nombre}'

if __name__ == '__main__':
    película1 = Película('prueba')
    print(película1)