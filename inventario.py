class Inventario:
    def __init__(self, nombre, cantidad):
        self._nombre = nombre
        self._cantidad = cantidad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def guardar_en_archivo(self):
        with open("inventario.txt", "a") as file:
            file.write(f"{self._nombre},{self._cantidad}\n")

    @staticmethod
    def mostrar_inventario():
        try:
            with open("inventario.txt", "r") as file:
                print("\n--- Inventario ---")
                for linea in file:
                    print(linea.strip())
        except FileNotFoundError:
            print("No hay productos registrados.")

    @staticmethod
    def menu_inventario():
        while True:
            print("\n--- Menú de Inventario ---")
            print("1. Agregar producto")
            print("2. Ver inventario")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre del producto: ")
                cantidad = input("Cantidad: ")
                producto = Inventario(nombre, cantidad)
                producto.guardar_en_archivo()
                print("Producto guardado.")
            elif opcion == "2":
                Inventario.mostrar_inventario()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")