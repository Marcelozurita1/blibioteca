# Importamos un módulo llamado 'tipo_categoria' que contiene una clase o funciones relacionadas con categorías de libros.
import tipo_categoria

# Definimos la clase 'Categoria_Libro', que hereda de 'tipo_categoria'.
class Categoria_Libro(tipo_categoria):
    # Constructor de la clase, se ejecuta cuando se crea un objeto 'Categoria_Libro'.
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro):
        # Llamamos al constructor de la clase padre 'tipo_categoria' y le pasamos 'id_tipo_categoria' para inicializarlo.
        super().__init__(id_tipo_categoria)
        
        # Inicializamos los atributos de la categoría del libro.
        self.id_categoria_libro = id_categoria_libro  # Identificador único de la categoría del libro.
        self.categoria_libro = categoria_libro        # Nombre o descripción de la categoría del libro.
