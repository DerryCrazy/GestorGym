class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni