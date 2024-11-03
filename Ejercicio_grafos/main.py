
from catalogo import *
from prenda_ropa import *

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Consultar Prendas")
    print("2. Buscar Prenda por ID")
    print("3. Buscar Prendas por Rango de Precio")
    print("4. Buscar Prendas por Rango de Stock")
    print("5. Menú de Desarrollador")
    print("6. Salir")

def mostrar_menu_desarrollador(detalle):
    print("\n--- Menú de Desarrollador ---")
    print("1. Añadir Prenda")
    print("2. Eliminar Prenda")
    print("3. Dibujar Árboles")
    print("4. Cambiar Listado a Detallado" if not detalle else "4. Cambiar Listado a Resumido")
    print("5. Regresar al Menú Principal")



if __name__ == "__main__":
    catalogo = Catalogo()
    detalle_listado = False  # Estado inicial del listado

    # Crear algunas prendas iniciales
    prendas = [
        PrendaRopa("Camiseta Básica", 20.0, 10, "ROJO", "CAMISETA", "ALGODON"),
        PrendaRopa("Pantalón Clásico", 30.0, 5, "AZUL", "PANTALON", "POLIESTER"),
        PrendaRopa("Abrigo de Invierno", 50.0, 2, "NEGRO", "ABRIGO", "LANA"),
        PrendaRopa("Vestido de Verano", 25.0, 8, "VERDE", "VESTIDO", "SEDA"),
        PrendaRopa("Camiseta de Rayas", 22.0, 15, "BLANCO", "CAMISETA", "ALGODON"),
        PrendaRopa("Pantalón de Tela", 35.0, 3, "GRIS", "PANTALON", "LANA"),
        PrendaRopa("Abrigo Ligero", 45.0, 6, "AZUL", "ABRIGO", "POLIESTER"),
        PrendaRopa("Vestido de Noche", 60.0, 4, "ROJO", "VESTIDO", "SEDA"),
        PrendaRopa("Camiseta Sin Mangas", 18.0, 12, "NEGRO", "CAMISETA", "ALGODON"),
        PrendaRopa("Pantalón Corto", 28.0, 8, "BEIGE", "PANTALON", "ALGODON"),
        PrendaRopa("Abrigo de Lluvia", 55.0, 1, "VERDE", "ABRIGO", "NYLON"),
        PrendaRopa("Vestido Floral", 40.0, 7, "MULTICOLOR", "VESTIDO", "ALGODON"),
        PrendaRopa("Camiseta Deportiva", 30.0, 10, "AZUL", "CAMISETA", "POLIESTER"),
        PrendaRopa("Pantalón de Jogging", 40.0, 5, "NEGRO", "PANTALON", "ALGODON"),
        PrendaRopa("Abrigo Acolchado", 70.0, 2, "ROJO", "ABRIGO", "PLUMA")
    ]

    # Insertar prendas en el catálogo
    for prenda in prendas:
        catalogo.añadir_prenda(prenda)

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nListado de prendas en el catálogo:")
            catalogo.listar_prendas(detalle_listado)

        elif opcion == '2':
            prenda_id = input("Ingrese el ID de la prenda que desea buscar: ")
            prenda = catalogo.buscar_prenda(prenda_id)
            print(prenda)

        elif opcion == '3':
            min_precio = float(input("Ingrese el precio mínimo: "))
            max_precio = float(input("Ingrese el precio máximo: "))
            print("\nPrendas en el rango de precio:")
            prendas_en_rango_precio = catalogo.arbol_precio.buscar_en_rango(min_precio, max_precio)
            for prenda in prendas_en_rango_precio:
                print(f"{prenda.nombre} - Precio: ${prenda.precio}")

        elif opcion == '4':
            min_stock = int(input("Ingrese el stock mínimo: "))
            max_stock = int(input("Ingrese el stock máximo: "))
            print("\nPrendas en el rango de stock:")
            prendas_en_rango_stock = catalogo.arbol_stock.buscar_en_rango(min_stock, max_stock, "stock")
            for prenda in prendas_en_rango_stock:
                print(f"{prenda.nombre} - Stock: {prenda.stock}")

        elif opcion == '5':
            while True:
                mostrar_menu_desarrollador(detalle_listado)
                opcion_dev = input("Seleccione una opción: ")

                if opcion_dev == '1':
                    # Añadir prenda
                    nombre = input("Ingrese el nombre de la prenda: ")
                    precio = float(input("Ingrese el precio de la prenda: "))
                    stock = int(input("Ingrese el stock de la prenda: "))
                    color = input("Ingrese el color de la prenda: ")
                    tipo = input("Ingrese el tipo de prenda: ")
                    material = input("Ingrese el material de la prenda: ")

                    nueva_prenda = PrendaRopa(nombre, precio, stock, color, tipo, material)
                    try:
                        catalogo.añadir_prenda(nueva_prenda)
                        print(f"Prenda '{nombre}' añadida al catálogo.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif opcion_dev == '2':
                    # Eliminar prenda
                    prenda_id = input("Ingrese el ID de la prenda que desea eliminar: ")
                    try:
                        catalogo.eliminar_prenda(prenda_id)
                        print(f"Prenda con ID {prenda_id} eliminada del catálogo.")
                    except KeyError as e:
                        print(e)

                elif opcion_dev == '3':
                    # Dibujar árboles
                    print("Dibujando árboles por precio y stock...")
                    catalogo.arbol_precio.dibujar_arbol(atributo="precio")
                    catalogo.arbol_stock.dibujar_arbol(atributo="stock")

                elif opcion_dev == '4':
                    # Cambiar listado
                    detalle_listado = not detalle_listado  # Alternar el modo de listado
                    estado = "detallado" if detalle_listado else "resumido"
                    print(f"El listado ha sido cambiado a modo {estado}.")

                elif opcion_dev == '5':
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

