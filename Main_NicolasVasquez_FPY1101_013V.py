
import datetime

libros = []
prestamos = []

def generar_sku(titulo, autor, anio):
    return f"{titulo[:3].upper()}-{autor[:3].upper()}-{anio}"

def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = input("Ingrese el año de publicación: ")
    sku = generar_sku(titulo, autor, anio)

    libro = {
        'titulo': titulo,
        'autor': autor,
        'anio': anio,
        'sku': sku
    }

    libros.append(libro)
    print(f"Libro registrado con éxito: {libro}")

def prestar_libro():
    usuario = input("Ingrese el nombre del usuario: ")
    sku = input("Ingrese el SKU del libro: ")

    libro_prestado = next((libro for libro in libros if libro['sku'] == sku), None)

    if libro_prestado:
        if any(prestamo['sku'] == sku for prestamo in prestamos):
            print("El libro ya está prestado.")
        else:
            prestamos.append({'usuario': usuario, 'sku': sku, 'fecha': datetime.datetime.now()})
            print(f"Libro prestado con éxito a {usuario}.")
    else:
        print("El libro no existe.")

def listar_libros():
    if libros:
        for libro in libros:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['anio']}, SKU: {libro['sku']}")
    else:
        print("No hay libros registrados.")

def imprimir_reporte_prestamos():
    if prestamos:
        for prestamo in prestamos:
            print(f"Usuario: {prestamo['usuario']}, SKU: {prestamo['sku']}, Fecha: {prestamo['fecha']}")
    else:
        print("No hay préstamos registrados.")

def salir():
    print("Saliendo del programa...")
    exit()

def main():
    opciones = {
        '1': registrar_libro,
        '2': prestar_libro,
        '3': listar_libros,
        '4': imprimir_reporte_prestamos,
        '5': salir
    }

    while True:
        print("\nOpciones:")
        print("1. Registrar libro")
        print("2. Prestar libro")
        print("3. Listar todos los libros")
        print("4. Imprimir reporte de préstamos")
        print("5. Salir del Programa")

        opcion = input("Seleccione una opción: ")

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()


