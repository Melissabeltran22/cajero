import os
import pyodbc
from getpass import getpass
from usuario import Usuario


class Transaccion:
    def __init__(self, usuario, conexion):
        self.usuario = usuario
        self.conexion = conexion

    def ejecutar_menu(self):
        while True:
            self.limpiar_pantalla()
            self.menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.retirar_dinero()
            elif opcion == "2":
                self.consultar_saldo()
            elif opcion == "3":
                self.consignar_dinero()
            elif opcion == "4":
                self.cambiar_clave()
            elif opcion == "5":
                self.consultar_transacciones()
            elif opcion == "6":
                print("Saliendo del menú transaccional...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        print("\nMenú de Transacciones")
        print("1. Retirar dinero")
        print("2. Consultar saldo")
        print("3. Consignar dinero")
        print("4. Cambiar clave")
        print("5. Consultar todas las transacciones")
        print("6. Salir")

    def retirar_dinero(self):
        cantidad = float(input("Ingrese el valor que desea retirar: $ "))
        self.usuario.retirar_dinero(cantidad)

    """def retirar_dinero(self):
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
            self.usuario.actualizar_saldo(nuevo_saldo)
            print(f"Su retiro por $ {cantidad} ha sido exitoso.")
            print(f"Nuevo saldo: $  {round(nuevo_saldo, 2)}")

            tipo_transaccion = "- R - Retiro"
            self.usuario.guardar_transaccion(tipo_transaccion, cantidad)
        else:
            print("No se pudo obtener el saldo. Intente nuevamente más tarde.")"""

    def consultar_saldo(self):
        saldo = self.usuario.consultar_saldo()
        if saldo is not None:
            print(f"Saldo actual: {saldo}")
        else:
            print("No se pudo obtener el saldo. Intente nuevamente más tarde.")

    def consignar_dinero(self):
        cantidad =float(input("Ingrese la cantidad a consignar : $ "))
        if cantidad <= 0:
            print("Ingrese una cantidad mayor que cero")
            return
        self.usuario.consignar_dinero(cantidad)

        """cursor = self.conexion.cursor()
        cantidad = float(input("Ingrese la cantidad a consignar: "))
        if cantidad <= 0:
            print("Ingrese una cantidad mayor que cero")
            return

        tipo_transaccion = "- C - Consignación"
        self.usuario.consignar_dinero(cantidad)

        print(f"Se han consignado $ {cantidad} correctamente.")

        # para que se guarde en transacciones:
        #self.usuario.guardar_transaccion(tipo_transaccion, cantidad)"""

    def cambiar_clave(self):
        #cursor = self.conexion.cursor()
        nueva_clave = getpass("Ingrese la nueva clave numérica de 4 dígitos: ")
        self.usuario.cambiar_clave(nueva_clave)
        print("Cambio de clave exitoso.")

    def consultar_transacciones(self):
        query = "SELECT * FROM Transacciones WHERE usuario = ?"
        cursor = self.conexion.cursor()
        cursor.execute(query, (self.usuario.nombre,))
        try:
            transacciones = cursor.fetchall()

            if transacciones:
                print("Transacciones del usuario:")
                for transaccion in transacciones:
                    fecha = transaccion[4]
                    tipo = transaccion[2]
                    monto = transaccion[3]
                    print(f"Fecha: {fecha}, Tipo: {tipo}, Monto: {monto}")

            else:
                print("El usuario no tiene transacciones registradas.")

        except pyodbc.Error as e:
            print("Error al consultar las transacciones:", e)



