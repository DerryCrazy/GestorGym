class Asistencia:
    def __init__(self, usuario, clase): #Constructor de la asistencia
        self.usuario = usuario
        self.clase = clase

    def mostrar_asistencia(self): #Muestra la asistencia
        return f"{self.usuario.nombre} asistió a {self.clase.nombre}"