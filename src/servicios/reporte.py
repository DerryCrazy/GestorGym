class Reporte:
    def __init__(self, titulo, contenido):
        self._titulo = titulo
        self._contenido = contenido

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_contenido(self):
        return self._contenido

    def set_contenido(self, contenido):
        self._contenido = contenido

    def guardar_en_archivo(self):
        with open("reportes.txt", "a") as file:
            file.write(f"{self._titulo}: {self._contenido}\n")

    @staticmethod
    def mostrar_reportes():
        try:
            with open("reportes.txt", "r") as file:
                print("\n--- Reportes ---")
                for linea in file:
                    print(linea.strip())
        except FileNotFoundError:
            print("No hay reportes registrados.")

    @staticmethod
    def menu_reportes():
        while True:
            print("\n--- Menú de Reportes ---")
            print("1. Crear reporte")
            print("2. Ver reportes")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                titulo = input("Título del reporte: ")
                contenido = input("Contenido del reporte: ")
                reporte = Reporte(titulo, contenido)
                reporte.guardar_en_archivo()
                print("Reporte guardado.")
            elif opcion == "2":
                Reporte.mostrar_reportes()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")