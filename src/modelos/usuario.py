from modelos.persona import Persona

class Usuario(Persona):#Heredando de la clase Persona
    contador_id = 1  # ID autoincremental

    def __init__(self, nombre, edad, correo): #Constructor
        super().__init__(Usuario.contador_id, nombre, edad, correo)
        self.clases_inscritas = [] #Añade el array de las clases a las que esta inscritas
        Usuario.contador_id += 1  # Incrementa el ID para el siguiente usuario

    def mostrar_info(self): #Muestra info
       return f"ID: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"