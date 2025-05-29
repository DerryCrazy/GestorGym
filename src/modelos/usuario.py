from modelos.persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, edad, dni, correo):
        super().__init__(nombre, edad, dni)
        self._correo = correo

    def get_correo(self):
        return self._correo

    def set_correo(self, correo):
        self._correo = correo

    def guardar_en_archivo(self):
        with open("usuarios.txt", "a") as file:
            file.write(f"{self._nombre},{self._edad},{self._dni},{self._correo}\n")

    @staticmethod
    def mostrar_usuarios():
        try:
            with open("usuarios.txt", "r") as file:
                for linea in file:
                    print(linea.strip())
        except FileNotFoundError:
            print("No hay usuarios registrados.")

    @staticmethod
    def menu_usuario():
        while True:
            print("\n--- Menú de Usuarios ---")
            print("1. Registrar usuario")
            print("2. Ver usuarios")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                dni = input("DNI: ")
                correo = input("Correo: ")
                usuario = Usuario(nombre, edad, dni, correo)
                usuario.guardar_en_archivo()
                print("Usuario registrado con éxito.")
            elif opcion == "2":
                Usuario.mostrar_usuarios()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")