from modelos.instructor import Instructor # Importacion

class Clases:
    contador_id = 1  # ID autoincremental

    def __init__(self, nombre, instructor, capacidad): #Constructor que se inicializa
        self.id_clase = Clases.contador_id
        self.nombre = nombre
        self.instructor = instructor
        self.capacidad = capacidad
        self.inscritos = []

        Clases.contador_id += 1  # Incrementa el ID para la siguiente clase

    def mostrar_inscritos(self): #Manda llamar la funcion
        if self.inscritos: #Si hay inscritos muestra la lista
            return [usuario.nombre for usuario in self.inscritos]
        return "❌ No hay usuarios inscritos en esta clase."