import paises  # Importa el módulo que contiene la clase Paises
import tipo_usuario  # Importa el módulo que contiene la clase Tipo_Usuario
import re  # Importa el módulo para expresiones regulares
from rut_chile import rut_chile  # Importa la funcionalidad para validar RUT chileno

class Usuario(paises.Paises, tipo_usuario.Tipo_Usuario):  # Asegúrate de que las clases sean correctas
    def __init__(self, id_usuario, nombre_usuario, correo_usuario, telefono_usuario, rut_usuario, codigo_pais, habilitado, id_tipo_usuario, fecha_creacion):
        # Llama al constructor de las clases base
        paises.Paises.__init__(self, codigo_pais)  # Inicializa la clase Paises con el código de país
        tipo_usuario.Tipo_Usuario.__init__(self, id_tipo_usuario)  # Inicializa la clase Tipo_Usuario con el ID del tipo de usuario
        
        # Inicializa los atributos específicos de la clase Usuario
        self.id_usuario = id_usuario  # ID del usuario
        self.nombre_usuario = nombre_usuario  # Nombre del usuario
        self.correo_usuario = correo_usuario  # Correo electrónico del usuario
        self.telefono_usuario = telefono_usuario  # Teléfono del usuario
        self.rut_usuario = rut_usuario  # RUT del usuario
        self.habilitado = habilitado  # Estado de habilitación del usuario (True o False)
        self.fecha_creacion = fecha_creacion  # Fecha de creación de la cuenta

    def validar_rut(self):
        # Método para validar el RUT chileno
        return rut_chile.is_valid_rut(self.rut_usuario)  # Utiliza la función importada para validar el RUT

    def validar_correo(self):
        # Método para validar el correo electrónico
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # Comprueba si el correo electrónico coincide con el patrón
        if re.fullmatch(regex, self.correo_usuario):  
            return True  # Devuelve True si el correo es válido
        else:
            return False  # Devuelve False si el correo no es válido
