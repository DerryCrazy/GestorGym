class Asistencia:
    def __init__(self, usuario, fecha):
        self._usuario = usuario
        self._fecha = fecha

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, usuario):
        self._usuario = usuario

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha):
        self._fecha = fecha

    def guardar_en_archivo(self):
        with open("asistencias.txt", "a") as file:
            file.write(f"{self._usuario},{self._fecha}\n")

    @staticmethod
    def mostrar_asistencias():
        try:
            with open("asistencias.txt", "r") as file:
                print("\n--- Asistencias ---")
                for linea in file:
                    print(linea.strip())
        except FileNotFoundError:
            print("No hay asistencias registradas.")

    @staticmethod
    def menu_asistencia():
        while True:
            print("\n--- Menú de Asistencia ---")
            print("1. Registrar asistencia")
            print("2. Ver asistencias")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                usuario = input("Nombre del usuario: ")
                fecha = input("Fecha (DD/MM/AAAA): ")
                asistencia = Asistencia(usuario, fecha)
                asistencia.guardar_en_archivo()
                print("Asistencia registrada.")
            elif opcion == "2":
                Asistencia.mostrar_asistencias()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")