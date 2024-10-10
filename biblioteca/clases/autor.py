# Importamos la clase 'datetime' para trabajar con fechas.
from datetime import datetime
# Importamos un módulo externo llamado paises que contiene países.
import paises

# Definimos la clase 'Autor' que hereda de la clase 'paises', lo que significa que 'Autor' tiene acceso a las propiedades y métodos de 'paises'.
class Autor(paises):
    # Este es el constructor de la clase, que define qué información tendrá cada autor cuando creemos un objeto 'Autor'.
    def __init__(self, id_autor, nombre_autor, seudonimo_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor):
        # Llamamos al constructor de la clase 'paises' para inicializar el código del país.
        super().__init__(codigo_pais)
        
        # Guardamos la información del autor en los atributos del objeto.
        self.id_autor = id_autor              
        self.nombre_autor = nombre_autor      
        self.seudonimo_autor = seudonimo_autor 
        self.fecha_nac = fecha_nac            
        self.fecha_def = fecha_def            
        self.biografia_autor = biografia_autor 
        self.foto_autor = foto_autor          

    # Método para convertir una fecha de un formato 'dd/mm/yyyy' a 'yyyy-mm-dd'.
    def manejo_fechas(fecha):
        # Convierte la fecha que recibe en texto al formato de fecha de Python.
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
        
        # Convierte esa fecha en un formato estándar 'yyyy-mm-dd' (más común en bases de datos).
        fecha_str = fecha_dt.strftime('%Y-%m-%d')
        
        # Retorna la fecha ya convertida en el nuevo formato.
        return fecha_str
