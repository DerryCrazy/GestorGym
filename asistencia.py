from datetime import datetime
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
                asistencias = [linea.strip() for linea in file]
                if asistencias:
                    Asistencia.mostrar_tabla(asistencias)
                else:
                    print("No hay asistencias registradas.")
        except FileNotFoundError:
            print("No hay asistencias registradas.")

    @staticmethod
    def mostrar_tabla(asistencias):
        print("\n{:<15} | {:<12}".format("Usuario", "Fecha"))
        print("-" * 30)
        for a in asistencias:
            usuario, fecha = a.split(",")
            print("{:<15} | {:<12}".format(usuario, fecha))


    @staticmethod
    def buscar_por_usuario(nombre_usuario):
        try:
            with open("asistencias.txt", "r") as file:
                asistencias = [linea.strip() for linea in file if linea.startswith(nombre_usuario + ",")]
                
                if asistencias:
                    print(f"\nAsistencias de {nombre_usuario}:")
                    for asistencia in asistencias:
                        print(asistencia)
                else:
                    print(f"No se encontraron asistencias para {nombre_usuario}.")
        except FileNotFoundError:
            print("No hay asistencias registradas.")

    @staticmethod
    def menu_asistencia():
        while True:
            print("\n--- Menú de Asistencia ---")
            print("1. Registrar asistencia")
            print("2. Ver todas las asistencias")
            print("3. Buscar asistencias por usuario")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                usuario = input("Nombre del usuario: ")
                fecha = input("Fecha (DD/MM/AAAA): ")
                # Validar formato de fecha
                try:
                    datetime.strptime(fecha, "%d/%m/%Y")
                    asistencia = Asistencia(usuario, fecha)
                    asistencia.guardar_en_archivo()
                    print("Asistencia registrada.")
                except ValueError:
                    print("⚠️ Fecha inválida. Usa el formato DD/MM/AAAA.")
            elif opcion == "2":
                Asistencia.mostrar_asistencias()
            elif opcion == "3":
                nombre = input("Ingresa el nombre del usuario: ").strip()
                Asistencia.buscar_por_usuario(nombre)
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
