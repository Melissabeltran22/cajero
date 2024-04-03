import os
import pyodbc
from datetime import datetime, timedelta


class Usuario:
    def __init__(self, nombre, conexion, cursor):
        self.nombre = nombre
        self.conexion = conexion
        self.cursor = cursor
        self.saldo = self.consultar_saldo()


    def consultar_saldo(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT saldo FROM Usuarios WHERE nombre= ?", (self.nombre,))
        saldo = cursor.fetchone()

        if saldo:
            return saldo[0]
        else:
            return None


    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def actualizar_saldo(self, nuevo_saldo):
        self.saldo = nuevo_saldo
        cursor = self.conexion.cursor()

    def consignar_dinero(self, cantidad):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE Usuarios SET saldo = saldo + ? WHERE nombre = ?", (cantidad, self.nombre))
        self.conexion.commit()
        print(f"Se han consignado $ {cantidad} correctamente.")
        tipo_transaccion = "- C - Consignación"
        self.guardar_transaccion(tipo_transaccion, cantidad)

    def retirar_dinero(self):
        #cursor  =self.conexion.cursor()
        saldo = float(self.usuario.consultar_saldo())
        if saldo is not None:
            print(f"Saldo actual : $  {round(saldo, 2)}")

            if saldo <= 0:
                print("Fondos insuficientes")
                return

            cantidad = float(input("Ingrese el valor que desea retirar: $ "))

            if cantidad > saldo:
                print("Fondos insuficientes")
                return

            nuevo_saldo = saldo - cantidad
            #self.usuario.actualizar_saldo(nuevo_saldo)
            cursor.execute("UPDATE Usuarios SET saldo = ? WHERE nombre = ?", (nuevo_saldo, self.nombre))
            self.conexion.commit()
            print(f"Su retiro por $ {cantidad} ha sido exitoso.")
            print(f"Nuevo saldo: $  {round(nuevo_saldo, 2)}")

            tipo_transaccion = "- R - Retiro"
            self.guardar_transaccion(tipo_transaccion, cantidad)
        else:
            print("No se pudo obtener el saldo. Intente nuevamente más tarde.")

    def cambiar_clave(self, nueva_clave):
        if not nueva_clave.isdigit() or len(nueva_clave) != 4:
            print("La nueva clave debe ser numérica de 4 dígitos.")
            return

        self.clave = nueva_clave
        print("Cambio de clave exitoso.")
        cursor = self.conexion.cursor()

    def consultar_transacciones(self):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT *FROM Transacciones WHERE usuario = ? AND fecha >= DATEADD(day, -3, GETDATE())"
            cursor.execute(query, (self.nombre,))
            transacciones = cursor.fetchall()


            if transacciones:
                print("Transacciones del usuario: ")
                for transaccion in transacciones:
                    tipo = transaccion[2]
                    monto = transaccion[3]
                    fecha = transaccion[4]

                    print(f"Fecha : {fecha}, Tipo: {tipo}, Monto: {monto}")

            else:
                print("El usuario no tiene transacciones registradas en los últimos 3 días.")
        except pyodbc.Error as e:
            print("Error en la consulta de transacciones: ", e)

        #self.usuario.consultar_transacciones(self.conexion)

    def guardar_transaccion(self, tipo, monto):
        try:
            query = "INSERT INTO Transacciones (usuario, tipo, monto, fecha) VALUES (?, ?, ?, ?)"
            fecha_actual = datetime.now()
            self.cursor.execute(query, (self.nombre, tipo, monto, fecha_actual))
            self.conexion.commit()
            print("Transacción guardada exitosamente.")
        except pyodbc.Error as e:
            print("Error al guardar la transacción:", e)