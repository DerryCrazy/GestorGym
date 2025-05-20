from modelos.persona import Persona

class Instructor(Persona):
    contador_id = 1  # ID autoincremental

    def __init__(self, nombre, edad, correo, especialidad):#Constructor 
        super().__init__(Instructor.contador_id, nombre, edad, correo) #Sobrecarga de constructor
        self.especialidad = especialidad #añade la especialidad
        Instructor.contador_id += 1  # Incrementa el ID para el siguiente instructor

    def mostrar_info(self):#Muestra la informacion  del instructor
        return f"ID: {self.id_persona}, Nombre: {self.nombre}, Especialidad: {self.especialidad}, Correo: {self.correo}"