class RegistroDuplicadoError(Exception):
    pass

class Galleta:
    def __init__(self, nombre, precio, peso):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que 0.")
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_info(self):
        return f"Galleta: {self.nombre} | Precio: Q{self.precio:.2f} | Peso: {self.peso}g"

#Herencia simple
class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        super().__init__(nombre, precio, peso)
        if cantidad_chispas <0:
            raise ValueError("La cantidad de chispas no puede ser negativa.")
        self.cantidad_chispas = cantidad_chispas

    def mostrar_info(self):
        return (f"Galleta con chispas: {self.nombre} | Precio: Q{self.precio:.2f} | "
                f"Peso: {self.peso}g | Chispas: {self.cantidad_chispas}")