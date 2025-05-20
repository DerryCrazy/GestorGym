class Pago:
    contador_id = 1  # ID autoincremental

    def __init__(self, usuario, monto): #Constructor con datos del pago
        self.id_pago = Pago.contador_id
        self.usuario = usuario
        self.monto = monto
        Pago.contador_id += 1  # Incrementa el ID para el siguiente pago

    def mostrar_pago(self): #Muestra la info del pago
        return f"Pago ID: {self.id_pago}, Usuario: {self.usuario.nombre}, Monto: ${self.monto}"