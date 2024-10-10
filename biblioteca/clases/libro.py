import autor  # Importa el módulo o la clase 'autor'

class Libro(autor):  # Define una clase llamada 'Libro' que hereda de 'autor'
    def __init__(self, isbn, titulo, id_autor):
        super().__init__(id_autor)  # Llama al constructor de la clase base 'autor' con 'id_autor'
        self.isbn = isbn  # Almacena el ISBN del libro
        self.titulo = titulo  # Almacena el título del libro
    
    def validar_isbn(self):
        # Método para validar el ISBN del libro
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True  # Devuelve True si el ISBN tiene entre 10 y 13 dígitos y es numérico
        else:
            return False  # Devuelve False si no cumple las condiciones
