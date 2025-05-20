class Inventario:
    def __init__(self):#Inicializa con un diccionario vacio
        self.equipos = {}

    def agregar_equipo(self, nombre, cantidad): #Agrega o actualiza la cantidad de equipos disp
        self.equipos[nombre] = self.equipos.get(nombre, 0) + cantidad

    def mostrar_inventario(self): #Muestra lo que hay en el diccionario
        return self.equipos