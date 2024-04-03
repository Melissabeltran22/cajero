import pyodbc
from usuario import Usuario
from transacciones import Transaccion
import os

class MiPlata:
    def __init__(self):
        self.conexion = pyodbc.connect(
            r"DRIVER={SQL Server};SERVER=MELISSA-LAPTOP\SQLEXPRESS01;DATABASE=dbCajero;Trusted_Connection=yes;")
        self.cursor = self.conexion.cursor()
        self.intentos_fallidos = {}

    def menu_inicio(self):
        print("Bienvenido a MiPlata")
        print("1. Iniciar sesión ")
        print("2. Registrarse ")
        print("3. Salir")

    def iniciar_sesion(self):
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        intentos_fallidos = self.obtener_intentos_fallidos(nombre_usuario)
        if intentos_fallidos and intentos_fallidos >= 3:
            print("Tu cuenta ha sido bloqueada por 24 horas. Por favor, comunícate con tu banco.")
            return

        if self.verificar_credenciales(nombre_usuario, contrasena):
            print("Inicio de sesión exitoso!")
            self.resetear_intentos_fallidos(nombre_usuario)
            usuario = Usuario(nombre_usuario, self.conexion, self.cursor)
            self.menu_transacciones(usuario)
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            self.registrar_intento_fallido(nombre_usuario)

    def verificar_credenciales(self, nombre_usuario, contrasena):
        self.cursor.execute("SELECT * FROM Usuarios WHERE nombre=? AND clave=?", (nombre_usuario, contrasena))
        return self.cursor.fetchone() is not None

    def obtener_intentos_fallidos(self, nombre_usuario):
        self.cursor.execute("SELECT intentos_fallidos FROM IntentosFallidos WHERE nombre= ?",
                            (nombre_usuario,))
        resultado = self.cursor.fetchone()
        return resultado[0] if resultado else 0

    def registrar_intento_fallido(self, nombre_usuario):
        intentos_fallidos = self.obtener_intentos_fallidos(nombre_usuario)
        if intentos_fallidos:
            intentos_fallidos += 1
            self.cursor.execute("UPDATE IntentosFallidos SET intentos_fallidos = ? WHERE nombre = ?", (intentos_fallidos, nombre_usuario))
        else:
            self.cursor.execute("INSERT INTO IntentosFallidos (nombre, intentos_fallidos) VALUES (?, 1)", (nombre_usuario,))
        self.conexion.commit()

    def resetear_intentos_fallidos(self, nombre_usuario):
        self.cursor.execute("DELETE FROM IntentosFallidos WHERE nombre= ?", (nombre_usuario,))
        self.conexion.commit()

    def menu_transacciones(self, usuario):
        transacciones = Transaccion(usuario, self.conexion)
        transacciones.ejecutar_menu()

        opcion = input("Seleccione una opción adicional: ")
        if opcion == "5":
            usuario.consultar_transacciones(self.conexion)
        else:
            print("Opción no válida.")

    def registrarse(self):
        print("Registro de nuevo usuario")
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        # Verificar si el nombre de usuario ya está en uso
        self.cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE nombre=?", (nombre_usuario,))
        if self.cursor.fetchone()[0] > 0:
            print("El nombre de usuario ya está en uso. Elija otro nombre de usuario.")
            return

        # Registrar el nuevo usuario
        self.cursor.execute("INSERT INTO Usuarios (nombre, clave) VALUES (?, ?)", (nombre_usuario, contrasena))
        self.conexion.commit()
        print("Usuario registrado exitosamente!")

    def run(self):
        while True:
            self.menu_inicio()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrarse()
            elif opcion == "3":
                print("Gracias por usar nuestros servicios. Hasta luego!")
                self.conexion.close()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mi_plata = MiPlata()
    mi_plata.run()
