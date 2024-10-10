class Paises():  # Define una clase llamada 'Paises'
    def __init__(self, codigo_pais, codigo_iso3_pais, nombre_pais, gentilicio_pais):
        # Este es el constructor que se ejecuta al crear una nueva instancia de la clase
        self.codigo_pais = codigo_pais  # Almacena el código del país (por ejemplo, un código de dos letras)
        self.codigo_iso3_pais = codigo_iso3_pais  # Almacena el código ISO de tres letras del país
        self.nombre_pais = nombre_pais  # Almacena el nombre completo del país
        self.gentilicio_pais = gentilicio_pais  # Almacena el gentilicio del país (por ejemplo, 'mexicano' para México)
