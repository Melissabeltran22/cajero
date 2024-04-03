create database dbCajero
use dbCajero


CREATE TABLE Usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    clave INT NOT NULL,
    saldo DECIMAL(10,2) NOT NULL CHECK (saldo >= 0))

	select *from Usuarios

INSERT INTO Usuarios VALUES ('Juan Pérez', 1234, 1000.00);
INSERT INTO Usuarios VALUES ('María González', 5678, 2500.50);
INSERT INTO Usuarios VALUES ('Pedro López', 9876, 500.00);
INSERT INTO Usuarios VALUES ('Ana Martínez', 5432, 1500.75);
INSERT INTO Usuarios VALUES ('Luisa Herrera', 7890, 300.25);
INSERT INTO Usuarios VALUES ('Carlos Sánchez', 2468, 2000.00);
INSERT INTO Usuarios VALUES ('Sofía Ramírez', 1357, 350.50);
INSERT INTO Usuarios VALUES ('Diego Rodríguez', 8023, 800.00);
INSERT INTO Usuarios VALUES ('Laura Díaz', 4567, 1200.00);
INSERT INTO Usuarios VALUES ('Javier Gómez', 9012, 600.75);
INSERT INTO Usuarios VALUES ('Elena Castro', 3456, 150.00);
INSERT INTO Usuarios VALUES ('Miguel Jiménez', 7891, 3000.00);
INSERT INTO Usuarios VALUES ('Sara Torres', 2345, 750.25);
INSERT INTO Usuarios VALUES ('Alejandro Ruiz', 6789, 200.50);
INSERT INTO Usuarios VALUES ('Paula Medina', 9871, 100.00);
INSERT INTO Usuarios VALUES ('Fernando Navarro', 5433, 1500.00);
INSERT INTO Usuarios VALUES ('Gabriela López', 1239, 3500.75);
INSERT INTO Usuarios VALUES ('Mario Pérez', 7856, 400.00);
INSERT INTO Usuarios VALUES ('Eva Fernández', 1356, 900.25);
INSERT INTO Usuarios VALUES ('Roberto García', 9870, 2200.50);
INSERT INTO Usuarios VALUES ('Natalia Martín', 2467, 175.00);
INSERT INTO Usuarios VALUES ('Adrián Soto', 3452, 6000.00);
INSERT INTO Usuarios VALUES ('Carolina Torres', 6781, 800.25);
INSERT INTO Usuarios VALUES ('Daniel Romero', 4321, 950.50);
INSERT INTO Usuarios VALUES ('Isabel Ortiz', 5679, 200.00);
INSERT INTO Usuarios VALUES ('Raúl Vargas', 8923, 300.75);
INSERT INTO Usuarios VALUES ('Lorena García', 6543, 750.00);
INSERT INTO Usuarios VALUES ('Juanita Pérez', 1789, 400.25);
INSERT INTO Usuarios VALUES ('Manuel Sánchez', 2901, 1100.50);
INSERT INTO Usuarios VALUES ('Cristina Rodríguez', 5671, 1750.00);
INSERT INTO Usuarios VALUES ('Pablo Díaz', 8021, 950.75);
INSERT INTO Usuarios VALUES ('Lucía Gómez', 1098, 2200.00);
INSERT INTO Usuarios VALUES ('Andrés López', 4326, 625.25);
INSERT INTO Usuarios VALUES ('Marina Flores', 7892, 1000.50);
INSERT INTO Usuarios VALUES ('Antonio Ramírez', 3458, 180.00);
INSERT INTO Usuarios VALUES ('Valentina Jiménez', 6780, 8000.00);
INSERT INTO Usuarios VALUES ('Mateo Torres', 4325, 900.25);
INSERT INTO Usuarios VALUES ('Patricia Ruiz', 9011, 300.50);
INSERT INTO Usuarios VALUES ('Jorge Medina', 1235, 200.00);
INSERT INTO Usuarios VALUES ('Ana Paula Navarro', 4569, 1500.75);
INSERT INTO Usuarios VALUES ('Diego Martínez', 8910, 2400.00);
INSERT INTO Usuarios VALUES ('Laura Gutiérrez', 1354, 750.25);
INSERT INTO Usuarios VALUES ('Marcos Castro', 7893, 1900.50);
INSERT INTO Usuarios VALUES ('Valeria Sánchez', 2460, 1100.00);
INSERT INTO Usuarios VALUES ('Eduardo Pérez', 5670, 325.25);
INSERT INTO Usuarios VALUES ('Camila Martín', 9023, 5000.00);
INSERT INTO Usuarios VALUES ('Santiago Ramírez', 6542, 600.50);
INSERT INTO Usuarios VALUES ('Victoria Díaz', 1090, 1800.75);
INSERT INTO Usuarios VALUES ('Gabriel López', 3457, 2200.00);
INSERT INTO Usuarios VALUES ('Diana Ortiz', 8901, 950.25);



CREATE TABLE IntentosFallidos (
    id INT,
    intentos_fallidos INT,
    CONSTRAINT FK_Usuarios_Id FOREIGN KEY (id) REFERENCES Usuarios(id));
ALTER TABLE IntentosFallidos
ADD nombre NVARCHAR(50);

select *from IntentosFallidos

CREATE TABLE Transacciones (
    id INT PRIMARY KEY IDENTITY(1,1),
    usuario NVARCHAR(100),
    tipo NVARCHAR(20),
    monto DECIMAL(10, 2),
    fecha DATETIME DEFAULT GETDATE()
);

);

