# Importamos un módulo llamado libro que contiene informacion de libros.
import libro

# Definimos la clase Biblioteca que manejará información y acciones dentro de una biblioteca.
class Biblioteca():
    # El constructor se ejecuta cuando se crea un objeto de 'Biblioteca' Inicializa la información básica de la biblioteca.
    def __init__(self, id_biblioteca, nombre_biblioteca, direccion_biblioteca, telefono_biblioteca):
        # Se guarda la información de la biblioteca en sus respectivos atributos.
        self.id_biblioteca = id_biblioteca              
        self.nombre_biblioteca = nombre_biblioteca      
        self.direccion_biblioteca = direccion_biblioteca 
        self.telefono_biblioteca = telefono_biblioteca  

    # Método para buscar un libro en la biblioteca usando su identificación.
 
    def buscar_libro(identificacion):
        pass  # funcion para buscar libros por un indentificativo".

    # funcion para prestar un libro de la biblioteca
    def prestar_libro(self):
        pass  

    # Método para devolver un libro a la biblioteca. También falta implementación.
    def devolver_libro(self):
        pass  # sirve para la funcionalidad futura de devolución de libros.
