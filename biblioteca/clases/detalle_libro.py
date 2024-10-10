# Importamos módulos 'libro' y 'editorial', que probablemente tienen funciones o datos sobre libros y editoriales.
import libro
import editorial

# Creamos la clase 'DetalleLibro' que hereda de 'libro' y 'editorial', es decir, que usa cosas de ambas clases.
class DetalleLibro(libro, editorial):
    # El constructor se ejecuta cuando hacemos un nuevo objeto de tipo 'DetalleLibro'.
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_ejemplares, ejemplares_disponibles):
        # Inicializamos la parte del libro usando su ISBN.
        libro.__init__(isbn)
        
        # Inicializamos la parte de la editorial usando el ID de la editorial.
        editorial.__init__(id_editorial)
        
        # Guardamos los datos del libro en los atributos.
        self.id_detalle_libro = id_detalle_libro               # ID único para identificar el libro.
        self.fecha_edicion = fecha_edicion                     # Cuándo se editó o publicó el libro.
        self.numero_paginas = numero_paginas                   # Cuántas páginas tiene el libro.
        self.id_categoria_libro = id_categoria_libro           # ID que dice a qué categoría pertenece (ej: ficción, ciencia).
        self.cantidad_ejemplares = cantidad_ejemplares         # Cuántos ejemplares de este libro hay en total.
        self.ejemplares_disponibles = ejemplares_disponibles   # Cuántos ejemplares están disponibles para prestar.

    # Método para actualizar cuántos libros están disponibles.
    # 'origen' nos dice si vamos a retirar o devolver libros, y 'cantidad' es cuántos.
    def actualizar_disponibilidad(self, origen, cantidad):
        # Revisamos que el total de ejemplares no sea menor que los disponibles más la cantidad.
        if(self.cantidad_ejemplares > self.ejemplares_disponibles + cantidad):
            # Si 'origen' es "retirar", significa que alguien quiere llevarse libros prestados.
            if(origen == "retirar"):
                # Si hay libros disponibles, restamos la cantidad que se va a prestar.
                if(self.ejemplares_disponibles > 0):
                    self.ejemplares_disponibles -= cantidad
                # Si no hay libros disponibles, mostramos un mensaje.
                else:
                    print("No hay ejemplares disponibles para préstamo.")
            # Si 'origen' no es "retirar", es porque están devolviendo libros, así que sumamos la cantidad.
            else:
                self.ejemplares_disponibles += cantidad
        # Si el total no cuadra, mostramos un mensaje de error.
        else:
            print("Hay un error en la cantidad de ejemplares.")
