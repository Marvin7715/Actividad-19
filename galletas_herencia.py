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

class Relleno:
    def __init__(self, sabor_relleno):
        if not sabor_relleno.strip():
            raise ValueError("El sabor del relleno no puede estar vacío.")
        self.sabor_relleno = sabor_relleno

    def describir_relleno(self):
        return f"Relleno de {self.sabor_relleno}"

#Herencia múltiple
class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_info(self):
        return (f"Galleta rellena: {self.nombre} | Precio: Q{self.precio:.2f} | "
                f"Peso: {self.peso}g | {self.describir_relleno()}")

galletas = []

def existe_nombre(nombre):
    return any(g.nombre.lower() == nombre.lower() for g in galletas)

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Entrada inválida. Ingresa un número válido.")

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Entrada inválida. Ingresa un número entero.")

def registrar_galleta():
    nombre = input("Nombre: ").strip()
    if existe_nombre(nombre):
        raise RegistroDuplicadoError(f"Ya existe una galleta con el nombre '{nombre}'.")
    precio = pedir_float("Precio: ")
    peso = pedir_float("Peso (g): ")
    galletas.append(Galleta(nombre, precio, peso))
    print("Galleta registrada.")

def registrar_galleta_chispas():
    nombre = input("Nombre: ").strip()
    if existe_nombre(nombre):
        raise RegistroDuplicadoError(f"Ya existe una galleta con el nombre '{nombre}'.")
    precio = pedir_float("Precio: ")
    peso = pedir_float("Peso (g): ")
    cantidad = pedir_int("Cantidad de chispas: ")
    galletas.append(GalletaChispas(nombre, precio, peso, cantidad))
    print("Galleta con chispas registrada.")

def registrar_galleta_rellena():
    nombre = input("Nombre: ").strip()
    if existe_nombre(nombre):
        raise RegistroDuplicadoError(f"Ya existe una galleta con el nombre '{nombre}'.")
    precio = pedir_float("Precio: ")
    peso = pedir_float("Peso (g): ")
    sabor = input("Sabor del relleno: ").strip()
    galletas.append(GalletaRellena(nombre, precio, peso, sabor))
    print("Galleta rellena registrada.")

def listar_galletas():
    if not galletas:
        print("No hay galletas registradas.")
        return
    for g in galletas:
        print(g.mostrar_info())

def buscar_galleta():
    nombre = input("Nombre a buscar: ").strip()
    encontrados = [g for g in galletas if g.nombre.lower() == nombre.lower()]
    if encontrados:
        for g in encontrados:
            print(g.mostrar_info())
    else:
        print("No se encontró la galleta.")

def eliminar_galleta():
    nombre = input("Nombre a eliminar: ").strip()
    global galletas
    nueva_lista = [g for g in galletas if g.nombre.lower() != nombre.lower()]
    if len(nueva_lista) == len(galletas):
        print(" No se encontró la galleta.")
    else:
        galletas = nueva_lista
        print("Galleta eliminada.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar galleta básica")
        print("2. Registrar galleta con chispas")
        print("3. Registrar galleta rellena")
        print("4. Listar galletas")
        print("5. Buscar por nombre")
        print("6. Eliminar por nombre")
        print("7. Salir")

        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                try:
                    registrar_galleta()
                except (ValueError, RegistroDuplicadoError) as e:
                    print(f"Error: {e}")
            case "2":
                try:
                    registrar_galleta_chispas()
                except (ValueError, RegistroDuplicadoError) as e:
                    print(f"Error: {e}")
            case "3":
                try:
                    registrar_galleta_rellena()
                except (ValueError, RegistroDuplicadoError) as e:
                    print(f"Error: {e}")
            case "4":
                listar_galletas()
            case "5":
                buscar_galleta()
            case "6":
                eliminar_galleta()
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida.")

menu()