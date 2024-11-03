# Tienda de ropa Alejandro Barreche Ruiz

# CATALOGO TIENDA DE ROPA

Bienvenido al proyecto **_Catálogo de Prendas de Vestir_**, una aplicación de consola diseñada para facilitar la gestión de un catálogo de ropa. Esta herramienta permite a los usuarios agregar, eliminar y buscar prendas de vestir de manera eficiente, utilizando estructuras de datos avanzadas como árboles AVL para optimizar la organización y recuperación de información.

## Funcionalidades

La aplicación incluye las siguientes características clave:

- *Gestión de Prendas*: Agrega, elimina y consulta prendas de vestir en el catálogo.
- *Búsquedas Avanzadas*: Busca prendas por ID, así como en rangos de precio y stock.
- *Visualización de Datos*: Alterna entre vistas resumidas y detalladas de las prendas.
- *Soporte para Desarrolladores*: Un menú dedicado que permite a los desarrolladores añadir y eliminar prendas, así como visualizar la estructura de datos interna mediante árboles AVL.

Los archivos que dividen el código son los siguientes:
1. **[prenda_de_ropa.py](prenda_de_ropa.py)**
2. **[catalogo.py](catalogo.py)**
3. **[arbol.py](arbol.py)**
4. **[main.py](main.py)**

## PRENDA DE ROPA

La clase PrendaRopa es una parte fundamental de un sistema de gestión de inventario de ropa, diseñada para manejar y organizar la información sobre las prendas de manera efectiva. A continuación, se detallan las principales utilidades de esta clase:

La clase PrendaRopa es fundamental en un sistema de gestión de inventario de ropa, proporcionando una estructura clara para almacenar y manipular información sobre cada prenda, incluyendo nombre, precio, stock, color, tipo y material. Utiliza UUIDs para garantizar identificadores únicos, lo que facilita la búsqueda y gestión de productos. Implementa controles de precios y stock mediante métodos específicos, evitando errores en las operaciones. Su diseño modular permite la integración con catálogos y sistemas más complejos, y sus métodos de representación mejoran la legibilidad de la información. En conjunto, PrendaRopa optimiza la eficiencia y claridad en la gestión del inventario.

**CLASE PRENDA DE ROPA**

- id_producto : UUID
- nombre: str
- precio: float
- stock: int
- color: str
- tipo de prenda: str
- material: str

## CATALOGO

La clase ***Catalogo*** es fundamental en la gestión de prendas de ropa, proporcionando una estructura organizada que permite _agregar, eliminar y listar prendas_ de manera eficiente.

Utiliza un diccionario para el almacenamiento rápido de prendas, mientras que la sincronización con árboles AVL garantiza un acceso ágil a través de operaciones logarítmicas. Sus métodos permiten añadir y eliminar prendas, previniendo duplicaciones y manteniendo la integridad de los datos. La clase también facilita la búsqueda y el listado, permitiendo mostrar prendas por nombre o detalle y ordenarlas por precio o stock.

Además, la funcionalidad de búsqueda en rango ayuda a los usuarios a encontrar productos dentro de su presupuesto. Diseñada para ser escalable y flexible, la clase Catalogo puede adaptarse a las necesidades cambiantes del sistema de inventario. En conjunto, proporciona una gestión eficiente y accesible de la información sobre prendas.

**CLASE CATALOGO**

- catalogo: dic
- arbol del precio: AVL
- arbol del stock: AVL

1. añadir_prenda()
2. eliminar_prenda()
3. lista_prendas()
4. buscar_prenda()
5. listar_prendas_por_precio()
6. listar_prendas_por_stock()
7. buscar_prendas_dentro_de_rango()


## ARBOL

La clase ***Arbol*** es crucial en la organización y optimización de la gestión de datos de las prendas, pues permite la estructuración eficiente mediante árboles AVL para mantener un equilibrio en las operaciones de búsqueda y almacenamiento, incluso con grandes volúmenes de datos.

### Atributos de la clase Arbol

- **raiz**: Nodo principal del árbol AVL.
- **altura**: Altura del árbol, utilizada para verificar el equilibrio en cada nodo.

### Métodos principales de la clase Arbol

1. **insertar(nodo)**: Inserta un nuevo nodo en el árbol AVL, garantizando el equilibrio tras la inserción.
2. **eliminar(nodo)**: Elimina un nodo específico del árbol y reajusta la estructura para mantener el equilibrio AVL.
3. **buscar(valor)**: Realiza una búsqueda en el árbol para encontrar un nodo con el valor especificado.
4. **obtener_altura(nodo)**: Calcula y devuelve la altura de un nodo, necesaria para evaluar el equilibrio en cada operación.
5. **balancear(nodo)**: Realiza operaciones de rotación (izquierda, derecha, doble izquierda-derecha, y doble derecha-izquierda) para mantener el árbol balanceado tras la inserción o eliminación de nodos.
6. **listar_en_orden()**: Retorna una lista ordenada de los elementos en el árbol, útil para listar los precios o el stock de manera organizada.
7. **buscar_en_rango(min_valor, max_valor)**: Realiza una búsqueda dentro de un rango específico, devolviendo todos los nodos cuyos valores estén comprendidos entre los límites dados.

### Ejemplo de Integración de Arbol en Catalogo

En el contexto de la clase ***Catalogo***, los árboles AVL se utilizan para organizar las prendas por atributos específicos (como precio o stock). Esto permite:

- **Acceso rápido**: Las operaciones de inserción, eliminación y búsqueda se realizan en tiempo logarítmico, lo cual es eficiente para manejar grandes cantidades de prendas.
- **Búsqueda y ordenamiento avanzados**: La integración con los métodos de búsqueda por rango y listado en orden permite a los usuarios obtener vistas personalizadas de las prendas según criterios específicos.


**EJEMPLO DE ARBOL**

[![Descripción de la imagen](https://github.com/user-attachments/assets/a9323e28-c314-4910-9882-d6cc93f225cd)](https://github.com/user-attachments/assets/a9323e28-c314-4910-9882-d6cc93f225cd)

## PASOS PARA EJECUTAR EL PROGRAMA

1. Asegúrate de tener Python instalado en tu máquina. Puedes verificar la instalación ejecutando `python --version` en tu terminal.
   
2. Clona el repositorio del proyecto usando el comando `git clone <url-del-repositorio>`.

3. Navega al directorio del proyecto con `cd <nombre-del-directorio>`.

4. Es posible que necesites instalar alguna librería específica como _matplotlib_, _networkx_, o _numpy_ que puedes hacer a través de la powershell `pip install <nombre de la libreria>`


















