from modelos.usuario import Usuario
from modelos.instructor import Instructor
from modelos.clases import Clases
from servicios.pago import Pago
from servicios.asistencia import Asistencia  # Importaciones de las demas clases
from servicios.inventario import Inventario
import os


# Listas globales para almacenar datos son temporales en lo que metemos achvs de txt
usuarios = []
instructores = []
clases_gym = []
pagos = []
asistencias = []
inventario_gimnasio = Inventario()

def menu_usuarios(): # Menu de usuarios
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n--- MENÚ DE USUARIOS ---") #Vistas de las opciones
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ") #Opcion sera introducida por usuario

        if opcion == "1": #Agregar usuario
            nombre = input("Nombre del usuario: ")
            edad = input("Edad: ")
            correo = input("Correo electrónico: ")
            usuario = Usuario(nombre, edad, correo)#Construye o inicializa un usuario con los parametros ya introducidos
            usuarios.append(usuario)
            print("✅ Usuario registrado con éxito.") #Ingresas los datos y se agrega al append de la lista de usuarios
            input("Presiona Enter para continuar...")

        elif opcion == "2": #Mostrar usuario
            if usuarios: #Verifica que en la lista de usuarios tenga un elemento al menos
                for usuario in usuarios: #Si es asi recorre toda la lista
                    print(usuario.mostrar_info()) #Y llama la funcion mostrar info por cada usuario
            else:
                print("❌ No hay usuarios registrados.")#Si no solo manda error
            input("Presiona Enter para continuar...")

        elif opcion == "3":#Borrar usuario
            if not usuarios:#Si esta vacio el arreglo muestra error
                print("❌ No hay usuarios registrados para eliminar.")
                continue#continua el codigo

            id_usuario = int(input("ID del usuario a eliminar: "))#Pide el id a eliminar
            for usuario in usuarios: #Recorre todos los usuarios
                if usuario.id_persona == id_usuario: #Si en un usuario hace match con el id que busca
                    usuarios.remove(usuario)#Remueve ese usuario de la lista
                    print(f"✅ Usuario {usuario.nombre} eliminado con éxito.") #Mensaje de exito
                    break#Termina
            else:#sI NO encuentra
                print("❌ Usuario no encontrado.")#Aviso
            input("Presiona Enter para continuar...")

        elif opcion == "4":#Opcion salir de este menu
            break

def menu_instructores():
    while True:#Mientras
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n---  MENÚ DE INSTRUCTORES ---") #Menu opc
        print("1. Registrar instructor")
        print("2. Mostrar instructores")
        print("3. Eliminar instructor")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")#Introduce opc

        if opcion == "1": #Agregar instructor
            nombre = input("Nombre del instructor: ")
            edad = input("Edad: ")
            correo = input("Correo electrónico: ")
            especialidad = input("Especialidad: ")
            instructor = Instructor(nombre, edad, correo, especialidad) #Genera un nuevo objeto de la clase instructor con los parametros introducidos
            instructores.append(instructor) #Agrega instructor a la lista
            print("✅ Instructor registrado con éxito.") #Mensajito 
            input("Presiona Enter para continuar...")

        elif opcion == "2": #Muestra instructores
            if instructores:#Si hay un dato
                for instructor in instructores: #Recorre con for la lista
                    print(instructor.mostrar_info()) #Muestra la info
            else:
                print("❌ No hay instructores registrados.") #No hay datos
            input("Presiona Enter para continuar...")

        elif opcion == "3":#Borrar instructor
            if not instructores: #Si no hay nada en instructores
                print("❌ No hay instructores registrados para eliminar.")
                continue

            id_instructor = int(input("ID del instructor a eliminar: "))#Pide el id del instructor
            for instructor in instructores: #Recorre la lista 
                if instructor.id_persona == id_instructor:#Si matchea una opc
                    instructores.remove(instructor) #Se elimina
                    print(f"✅ Instructor {instructor.nombre} eliminado con éxito.")#Mensajito
                    break
            else:#Si no encuentra le dice jeje
                print("❌ Instructor no encontrado.")
            input("Presiona Enter para continuar...")

        elif opcion == "4": #Salir
            break

def menu_clases():#Menu de clases
    while True: #Mientras 
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n--- MENÚ DE CLASES ---")#Menu
        print("1. Registrar clase")
        print("2. Mostrar clases")
        print("3. Eliminar clase")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ") #Captura opc

        if opcion == "1": #Ingresa una clase
            nombre = input("Nombre de la clase: ")
            id_instructor = int(input("ID del instructor asignado: "))
            capacidad = int(input("Capacidad máxima: "))
            instructor_obj = next((i for i in instructores if i.id_persona == id_instructor), None)#Registra el instructor a la clase con el id
            if instructor_obj:#sI Encuentra al instructor en la lista de registrados
                clase = Clases(nombre, instructor_obj, capacidad) #Genera la nueva clase con los parametros
                clases_gym.append(clase)#La mete al array
                print("✅ Clase registrada con éxito.") #Mensajito
            else:#Si no hay instructor
                print("❌ Instructor no encontrado.")
            input("Presiona Enter para continuar...")

        elif opcion == "2": #mostrar clase
            if clases_gym: #Si hay un dato en el array
                for clase in clases_gym: #Lo recorre
                    print(f"ID: {clase.id_clase}, Nombre: {clase.nombre}, Instructor: {clase.instructor.nombre}")#Y muestra las clases que hay
            else:#Si no 
                print("❌ No hay clases registradas.")
            input("Presiona Enter para continuar...")

        elif opcion == "3":#Borrar clase
            if not clases_gym: #Checa que no este vacio el array y si si ps manda eror
                print("❌ No hay clases registradas para eliminar.")
                continue

            id_clase = int(input("ID de la clase a eliminar: "))#Si no, pide el id de la clase a eliminar
            for clase in clases_gym:#Recorre el array
                if clase.id_clase == id_clase:#Match con el id
                    clases_gym.remove(clase)#Se elimina la clase
                    print(f"✅ Clase {clase.nombre} eliminada con éxito.")#Mensajito
                    break
            else:#Si no coincide el id, manda error
                print("❌ Clase no encontrada.")
            input("Presiona Enter para continuar...")

        elif opcion == "4":#Sale del menu
            break

def menu_pagos():#Menu de pagos
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n--- MENÚ DE PAGOS ---")
        print("1. Registrar pago")
        print("2. Mostrar pagos")
        print("3. Eliminar pago")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ") #opc introducida

        if opcion == "1": #Registro de pago
            id_usuario = int(input("ID del usuario: "))
            monto = float(input("Monto a pagar: "))
            usuario_obj = next((u for u in usuarios if u.id_persona == id_usuario), None) #Busca a ver si existe ese usuario y en caso de que si
            if usuario_obj:
                pago = Pago(usuario_obj, monto) #Inicializa el pago
                pagos.append(pago) #Lo agrega a el array
                print("✅ Pago registrado con éxito.") #Mensaje
            else:#Si no
                print("❌ Usuario no encontrado.")
            input("Presiona Enter para continuar...")

        elif opcion == "2":# Mostrar un vaoucher de pago
            if pagos:#Si esta un elemento al menos en el array
                for pago in pagos: #Lo recorre
                    print(pago.mostrar_pago())#Muestra la info
            else:
                print("❌ No hay pagos registrados.")#Si no
            input("Presiona Enter para continuar...")

        elif opcion == "3": #Borrar un pago
            if not pagos:#checa que no este vacio
                print("❌ No hay pagos registrados para eliminar.")
                continue

            id_pago = int(input("ID del pago a eliminar: ")) #Pide el id
            for pago in pagos:#recorre array
                if pago.id_pago == id_pago:#Si matchea
                    pagos.remove(pago)#Elimina
                    print("✅ Pago eliminado con éxito.")#Mensaaaaje
                    break
            else:
                print("❌ Pago no encontrado.")#Si no hay id
            input("Presiona Enter para continuar...")

        elif opcion == "4":
            break

def menu_inventario():#Inventario 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n---  MENÚ DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Agregar equipo")
        print("3. Actualizar equipo")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")#Opc

        if opcion == "1":#mOSTRAR inventario actual
            print(inventario_gimnasio.mostrar_inventario()) #Lo muestra
            input("Presiona Enter para continuar...")

        elif opcion == "2":#Agregar equipo
            equipo = input("Nombre del equipo: ")
            cantidad = int(input("Cantidad a agregar: "))
            inventario_gimnasio.agregar_equipo(equipo, cantidad) #agrega al array
            print("✅ Equipo agregado al inventario.")
            input("Presiona Enter para continuar...")

        elif opcion == "3":
            equipo = input("Nombre del equipo: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario_gimnasio.equipos[equipo] = cantidad#Actualiza cantidad
            print("✅ Inventario actualizado.")
            input("Presiona Enter para continuar...")

        elif opcion == "4":#Salir
            break

def menu_asistencia():#ASISTENCIA
    while True: #mientras
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola antes de mostrar opciones
        print("\n--- MENÚ DE ASISTENCIA ---")
        print("1. Registrar asistencia")
        print("2. Mostrar asistencias")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción: ")#Opcion

        if opcion == "1": #Registrar asistencia
            id_usuario = int(input("ID del usuario: "))
            id_clase = int(input("ID de la clase: "))
            usuario_obj = next((u for u in usuarios if u.id_persona == id_usuario), None) #Tienen que encontrar el siguiente de estos
            clase_obj = next((c for c in clases_gym if c.id_clase == id_clase), None)

            if usuario_obj and clase_obj: #sI Las dos cosas coinciden
                asistencia = Asistencia(usuario_obj, clase_obj) #Se genera asistencia
                asistencias.append(asistencia) #Se agrega al array
                print(f"✅ Asistencia registrada: {usuario_obj.nombre} asistió a {clase_obj.nombre}.") #Se muestra mensaje
            else:
                print("❌ Usuario o clase no encontrados.")#Algun error
            input("Presiona Enter para continuar...")

        elif opcion == "2": #Mostrar la asistencia
            if asistencias:#Si tiene algun dato en el array reviso
                for asistencia in asistencias:#En el for recorre toda la lista
                    print(asistencia.mostrar_asistencia()) #Muestra la asistencia
            else:
                print("❌ No hay asistencias registradas.")#No hay
            input("Presiona Enter para continuar...")

        elif opcion == "3": #Salir
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")


def mostrar_menu(): #Menu principal a submenus
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Usuarios")
        print("2. Instructores")
        print("3. Clases")
        print("4. Pagos")
        print("5. Inventario")
        print("6. Asistencia")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")#Opcion introducida

        if opcion == "1":
            menu_usuarios()#Llama las funciones de los otros menus anteriorressss
        elif opcion == "2":
            menu_instructores()
        elif opcion == "3":
            menu_clases()
        elif opcion == "4":
            menu_pagos()
        elif opcion == "5":
            menu_inventario()
        elif opcion == "6":
            menu_asistencia()
        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")#oPCION default

if __name__ == "__main__":
    mostrar_menu() #Ejecuta todo en base al menu principal:D