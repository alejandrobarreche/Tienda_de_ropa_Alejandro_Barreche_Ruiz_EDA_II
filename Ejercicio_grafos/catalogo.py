from prenda_ropa import PrendaRopa
from arbol import AVL

class Catalogo:
    def __init__(self):
        # Diccionario que almacena las prendas, usando id_producto como clave
        self.catalogo = {}
        # Crear árboles AVL para organizar prendas por precio y stock
        self.arbol_precio = AVL()
        self.arbol_stock = AVL()

    def añadir_prenda(self, prenda):
        """Añade una prenda al catálogo si es una instancia de PrendaRopa y su ID no existe ya."""
        if isinstance(prenda, PrendaRopa):  # Verificar si es una prenda válida
            if prenda.id_producto in self.catalogo:
                raise ValueError(f"La prenda con ID {prenda.id_producto} ya existe en el catálogo.")
            self.catalogo[prenda.id_producto] = prenda  # Añadir al catálogo
            # Insertar la prenda en los árboles AVL según precio y stock
            self.arbol_precio.insertar(prenda, atributo="precio")
            self.arbol_stock.insertar(prenda, atributo="stock")
        else:
            raise TypeError("El objeto no es una instancia de PrendaRopa.")

    def eliminar_prenda(self, producto_id):
        """Elimina una prenda del catálogo por su ID y la remueve de los árboles AVL."""
        prenda = self.catalogo.pop(producto_id, None)  # Remover del catálogo
        if prenda:
            # Eliminar del árbol AVL según precio y stock
            self.arbol_precio.eliminar(prenda, atributo="precio")
            self.arbol_stock.eliminar(prenda, atributo="stock")
        else:
            raise KeyError(f"No se encontró ninguna prenda con ID {producto_id} en el catálogo.")

    def listar_prendas(self, detalles=False):
        """Lista todas las prendas en el catálogo."""
        if detalles:
            for prenda in self.catalogo.values():
                print(prenda)  # Mostrar detalles completos de cada prenda
        else:
            for index, prenda in enumerate(self.catalogo.values()):
                print(f"{index+1}: {prenda.nombre}")  # Mostrar solo el nombre de cada prenda

    def buscar_prenda(self, producto_id):
        """Busca una prenda en el catálogo por su ID."""
        return self.catalogo.get(producto_id, None)  # Retorna la prenda si existe

    def listar_por_precio(self):
        """Lista las prendas ordenadas por precio usando el árbol AVL."""
        return self.arbol_precio.listar_prendas()

    def listar_por_stock(self):
        """Lista las prendas ordenadas por stock usando el árbol AVL."""
        return self.arbol_stock.listar_prendas()

    # Metodo auxiliar para buscar prendas en un rango de precios o stock
    def _buscar_en_rango(self, nodo, min_precio, max_precio, atributo):
        resultados = []
        if nodo:
            # Buscar en el subárbol izquierdo si el nodo cumple con el mínimo
            if getattr(nodo.prenda, atributo) >= min_precio:
                resultados.extend(self._buscar_en_rango(nodo.left, min_precio, max_precio, atributo))
            # Añadir el nodo si está dentro del rango
            if min_precio <= getattr(nodo.prenda, atributo) <= max_precio:
                resultados.append(nodo.prenda)
            # Buscar en el subárbol derecho si el nodo cumple con el máximo
            if getattr(nodo.prenda, atributo) <= max_precio:
                resultados.extend(self._buscar_en_rango(nodo.right, min_precio, max_precio, atributo))
        return resultados

    # Búsqueda pública de prendas en un rango específico de precios o stock
    def buscar_en_rango(self, min_precio, max_precio, atributo="precio"):
        return self._buscar_en_rango(self.root, min_precio, max_precio, atributo)

