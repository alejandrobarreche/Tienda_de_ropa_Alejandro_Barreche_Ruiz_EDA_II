import uuid

class PrendaRopa:
    def __init__(self, nombre, precio, stock, color, tipo_de_prenda, material):
        self._id_producto = str(uuid.uuid4())  # Genera un UUID único
        self.nombre = nombre
        self._precio = precio
        self._stock = stock
        self.color = color
        self.tipo_de_prenda = tipo_de_prenda
        self.material = material

    @property
    def id_producto(self):
        """Getter para id_producto."""
        return self._id_producto

    @property
    def precio(self):
        """Getter para precio."""
        return self._precio

    @precio.setter
    def precio(self, precio):
        """Setter para precio."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    @property
    def stock(self):
        """Getter para stock."""
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Setter para stock."""
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = stock

    def __repr__(self):
        return f"{self.nombre} \t(Precio: {self.precio}\t Stock: {self.stock}) ID: {self._id_producto}"

    def __str__(self):
        return f"{self.nombre} \t(Precio: {self.precio}\t Stock: {self.stock}) ID: {self._id_producto}"
