from modelos.usuario import Usuario
from servicios.pago import Pago
from servicios.reporte import Reporte
from servicios.inventario import Producto
from servicios.asistencia import Asistencia

def main():
    while True:
        print("1. Menú Usuarios")
        print("2. Menú Pagos")
        print("3. Menú Reportes")
        print("4. Menú Inventario")
        print("5. Menú Asistencia")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            Usuario.menu_usuario()
        elif opcion == "2":
            Pago.menu_pago()
        elif opcion == "3":
            Reporte.menu_reportes()
        elif opcion == "4":
            Producto.menu_inventario()
        elif opcion == "5":
            Asistencia.menu_asistencia()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()