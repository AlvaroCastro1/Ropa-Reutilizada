CREATE DATABASE Ropa;
USE ROPA;
CREATE TABLE Clientes (
    IDCliente INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30),
    ApellidoM VARCHAR(30),
    ApellidoP VARCHAR(30),
    Telefono VARCHAR(10),
    Email VARCHAR(30) UNIQUE,
    Contrasena varchar(30),
    Monedero DECIMAL(4,2)
) ENGINE=InnoDB;

CREATE TABLE Donacion (
    IDDonacion INT PRIMARY KEY AUTO_INCREMENT,
    FechaDeDonacion DATETIME
) ENGINE=InnoDB;

CREATE TABLE CDonante (
    IDDonante INT PRIMARY KEY AUTO_INCREMENT,
    IDCliente1 INT,
    IDDonacion1 INT,
    PuntosAgregados DECIMAL(10,2),
    FOREIGN KEY (IDCliente1) REFERENCES Clientes(IDCliente),
    FOREIGN KEY (IDDonacion1) REFERENCES Donacion(IDDonacion)
) ENGINE=InnoDB;

CREATE TABLE IProductos (
    IDIProducto INT PRIMARY KEY AUTO_INCREMENT,
    Talla VARCHAR(20),
    Color VARCHAR(15),
    Genero VARCHAR(20),
    Material VARCHAR(30),
    Tipo VARCHAR(30),
    Descripcion VARCHAR(300),
    Precio DECIMAL(10,2),
    PuntosC DECIMAL(10,2),
    Destino VARCHAR(30)
) ENGINE=InnoDB;

CREATE TABLE ImagenesProductos (
    IDImagen INT PRIMARY KEY AUTO_INCREMENT,
    IDIProducto INT,
    URLImagen VARCHAR(1000),
    FOREIGN KEY (IDIProducto) REFERENCES IProductos(IDIProducto)
) ENGINE=InnoDB;

CREATE TABLE Apartado(
    IDApartado INT PRIMARY KEY AUTO_INCREMENT,
    FHDeApartado DATETIME,
    ProductosT INT,
    CantidadT DECIMAL(4,2)
)ENGINE=InnoDB;

CREATE TABLE AProducto (
    IDAProducto INT PRIMARY KEY AUTO_INCREMENT,
    IDIProducto1 INT,
    IDApartado1 INT,
    IDCliente2 INT,
    FOREIGN KEY (IDIProducto1) REFERENCES IProductos(IDIProducto),
    FOREIGN KEY (IDApartado1) REFERENCES Apartado(IDApartado),
    FOREIGN KEY (IDCliente2) REFERENCES Clientes(IDCliente)
) ENGINE=InnoDB;

CREATE TABLE Canjeo(
    IDCanjeo INT PRIMARY KEY AUTO_INCREMENT,
    IDIProducto2 INT,
    IDCliente3 INT,
    FHCanjeo DATETIME,
    FOREIGN KEY (IDIProducto2) REFERENCES IProductos(IDIProducto),
    FOREIGN KEY (IDCliente3) REFERENCES Clientes(IDCliente)
)ENGINE=InnoDB;