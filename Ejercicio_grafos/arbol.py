from prenda_ropa import PrendaRopa
import networkx as nx
import matplotlib.pyplot as plt


# Nodo del árbol AVL
class Node:
    def __init__(self, prenda):
        self.prenda = prenda  # Objeto PrendaRopa asociado
        self.nombre = prenda.nombre  # Nombre de la prenda
        self._parent = None
        self._left = None
        self._right = None
        self.height = 1  # Altura inicial del nodo

    # GETTERS Y SETTERS

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is not None:
            node._parent = self
        self._right = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is not None:
            node._parent = self
        self._left = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is not None:
            self._parent = node
            self.height = self.parent.height + 1
        else:
            self.height = 1


# Árbol AVL para almacenar las prendas
class AVL:
    def __init__(self):
        self.root = None

    # Retorna altura de un nodo
    def _altura(self, nodo):
        return nodo.height if nodo else 0

    # Actualiza la altura del nodo
    def _actualizar_altura(self, nodo):
        if nodo:
            nodo.height = 1 + max(self._altura(nodo.left), self._altura(nodo.right))

    # Calcula balance del nodo
    def _balance(self, nodo):
        return self._altura(nodo.left) - self._altura(nodo.right) if nodo else 0

    # Rotación derecha
    def _rotar_derecha(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    # Rotación izquierda
    def _rotar_izquierda(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    # Inserta un nodo en el árbol AVL
    def _insertar(self, nodo, prenda, atributo):
        if not nodo:
            return Node(prenda)

        # Inserción según el atributo
        if getattr(prenda, atributo) < getattr(nodo.prenda, atributo):
            nodo.left = self._insertar(nodo.left, prenda, atributo)
        else:
            nodo.right = self._insertar(nodo.right, prenda, atributo)

        # Actualiza altura y balancea
        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        # Rotaciones según el balance
        if balance > 1 and getattr(prenda, atributo) < getattr(nodo.left.prenda, atributo):
            return self._rotar_derecha(nodo)
        if balance < -1 and getattr(prenda, atributo) > getattr(nodo.right.prenda, atributo):
            return self._rotar_izquierda(nodo)
        if balance > 1 and getattr(prenda, atributo) > getattr(nodo.left.prenda, atributo):
            nodo.left = self._rotar_izquierda(nodo.left)
            return self._rotar_derecha(nodo)
        if balance < -1 and getattr(prenda, atributo) < getattr(nodo.right.prenda, atributo):
            nodo.right = self._rotar_derecha(nodo.right)
            return self._rotar_izquierda(nodo)

        return nodo

    # Elimina un nodo del árbol AVL
    def _eliminar(self, nodo, prenda, atributo):
        if not nodo:
            return nodo

        # Encuentra y elimina el nodo
        if getattr(prenda, atributo) < getattr(nodo.prenda, atributo):
            nodo.left = self._eliminar(nodo.left, prenda, atributo)
        elif getattr(prenda, atributo) > getattr(nodo.prenda, atributo):
            nodo.right = self._eliminar(nodo.right, prenda, atributo)
        else:
            if not nodo.left:
                return nodo.right
            elif not nodo.right:
                return nodo.left

            # Nodo con dos hijos
            temp = self._min_value_node(nodo.right)
            nodo.prenda = temp.prenda
            nodo.right = self._eliminar(nodo.right, temp.prenda, atributo)

        # Actualiza altura y balancea
        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        # Rotaciones según el balance
        if balance > 1 and self._balance(nodo.left) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.left) < 0:
            nodo.left = self._rotar_izquierda(nodo.left)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.right) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.right) > 0:
            nodo.right = self._rotar_derecha(nodo.right)
            return self._rotar_izquierda(nodo)

        return nodo

    # Nodo de valor mínimo
    def _min_value_node(self, nodo):
        current = nodo
        while current.left:
            current = current.left
        return current

    def eliminar(self, prenda, atributo="precio"):
        self.root = self._eliminar(self.root, prenda, atributo)

    # Busca prendas en un rango de precios
    def _buscar_en_rango(self, nodo, min_precio, max_precio, atributo):
        resultados = []
        if nodo:
            if getattr(nodo.prenda, atributo) >= min_precio:
                resultados.extend(self._buscar_en_rango(nodo.left, min_precio, max_precio, atributo))
            if min_precio <= getattr(nodo.prenda, atributo) <= max_precio:
                resultados.append(nodo.prenda)
            if getattr(nodo.prenda, atributo) <= max_precio:
                resultados.extend(self._buscar_en_rango(nodo.right, min_precio, max_precio, atributo))
        return resultados

    def buscar_en_rango(self, min_precio, max_precio, atributo="precio"):
        return self._buscar_en_rango(self.root, min_precio, max_precio, atributo)

    def insertar(self, prenda, atributo="precio"):
        self.root = self._insertar(self.root, prenda, atributo)

    # Recorrido inorden
    def _recorrido_inorden(self, nodo):
        return self._recorrido_inorden(nodo.left) + [nodo.prenda] + self._recorrido_inorden(nodo.right) if nodo else []

    def listar_prendas(self):
        return self._recorrido_inorden(self.root)

    # Dibuja el árbol AVL
    def dibujar_arbol(self, atributo="precio"):
        G = nx.DiGraph()
        self.posiciones = {}
        self._agregar_nodos_y_aristas(G, self.root, pos=(0, 0), nivel=0, distancia=2.0)

        labels = {nodo: f"{nodo.prenda.nombre}\n{atributo.capitalize()}: {getattr(nodo.prenda, atributo)}" for nodo in
                  G.nodes()}

        # Visualización
        plt.figure(figsize=(12, 8))
        nx.draw(
            G, pos=self.posiciones,
            with_labels=True,
            labels=labels,
            node_size=1000,
            node_color='lightblue',
            font_size=8
        )
        plt.title(f"Árbol AVL de Prendas (Ordenado por {atributo.capitalize()})")
        plt.axis('off')
        plt.show()

    # Agrega nodos y aristas en el gráfico
    def _agregar_nodos_y_aristas(self, G, nodo, pos, nivel, distancia):
        if nodo:
            G.add_node(nodo)
            self.posiciones[nodo] = pos
            nivel_distancia = distancia / (nivel + 1)

            if nodo.left:
                pos_izquierdo = (pos[0] - nivel_distancia, pos[1] - 1)
                G.add_edge(nodo, nodo.left)
                self._agregar_nodos_y_aristas(G, nodo.left, pos_izquierdo, nivel + 1, distancia)

            if nodo.right:
                pos_derecho = (pos[0] + nivel_distancia, pos[1] - 1)
                G.add_edge(nodo, nodo.right)
                self._agregar_nodos_y_aristas(G, nodo.right, pos_derecho, nivel + 1, distancia)
