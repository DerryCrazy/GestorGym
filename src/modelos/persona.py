#Clase base para heredar a usuario e instructor
class Persona:
    def __init__(self, id_persona, nombre, edad, correo): #Constructor 
        self.id_persona = id_persona
        self.nombre = nombre
        self.edad = edad #Constructor de la clase persona
        self.correo = correo

    def mostrar_info(self):# Devuelve toda la info que contiene esa persona 
        return f"ID: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"
