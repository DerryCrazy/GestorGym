class Pago:
    def __init__(self, cliente, monto):
        self._cliente = cliente
        self._monto = monto

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_monto(self):
        return self._monto

    def set_monto(self, monto):
        self._monto = monto

    def guardar_en_archivo(self):
        with open("pagos.txt", "a") as file:
            file.write(f"{self._cliente},{self._monto}\n")

    @staticmethod
    def mostrar_pagos():
        try:
            with open("pagos.txt", "r") as file:
                print("\n--- Lista de Pagos ---")
                for linea in file:
                    print(linea.strip())
        except FileNotFoundError:
            print("No hay pagos registrados.")

    @staticmethod
    def menu_pago():
        while True:
            print("\n--- Menú de Pagos ---")
            print("1. Registrar pago")
            print("2. Ver pagos")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                cliente = input("Nombre del cliente: ")
                monto = input("Monto pagado: ")
                pago = Pago(cliente, monto)
                pago.guardar_en_archivo()
                print("Pago registrado.")
            elif opcion == "2":
                Pago.mostrar_pagos()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")