import re  # Importa el módulo 're' que permite trabajar con expresiones regulares

class Editorial():  # Define una clase llamada 'Editorial'
    def __init__(self, id_editorial, nombre_editorial, fecha_fundacion, codigo_pais, telefono_contacto, correo_contacto):
        # Este es el constructor que inicializa las propiedades de la clase cuando se crea una nueva instancia.
        self.id_editorial = id_editorial  # ID de la editorial
        self.nombre_editorial = nombre_editorial  # Nombre de la editorial
        self.fecha_fundacion = fecha_fundacion  # Fecha de fundación de la editorial
        self.codigo_pais = codigo_pais  # Código del país de la editorial
        self.telefono_contacto = telefono_contacto  # Número de teléfono de contacto
        self.correo_contacto = correo_contacto  # Correo electrónico de contacto
    
    def validar_correo(self):
        # Método para validar el correo electrónico de la editorial
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  # Expresión regular para el formato de un correo electrónico
        # Verifica si el correo electrónico de contacto coincide con la expresión regular
        if re.fullmatch(regex, self.correo_contacto):
            return True  # Si el correo es válido, devuelve True
        else:
            return False  # Si el correo no es válido, devuelve False
