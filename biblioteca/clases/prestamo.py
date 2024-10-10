from datetime import datetime, timedelta
from auxiliares import constantes  # Importa constantes que probablemente contengan días festivos
import detalle_libro  # Importa el módulo que maneja detalles del libro
import usuario  # Importa el módulo que maneja detalles del usuario

class Prestamo(detalle_libro.DetalleLibro, usuario.Usuario):  # Asegúrate de que las clases sean correctas
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo=None, fecha_devolucion=None, fecha_devuelto=None, cantidad_solicitada=1):
        # Llama al constructor de las clases base
        detalle_libro.DetalleLibro.__init__(self, isbn)  # Inicializa con el ISBN del libro
        usuario.Usuario.__init__(self, id_usuario)  # Inicializa con el ID del usuario
        self.id_prestamo = id_prestamo  # ID del préstamo
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo else datetime.now()  # Fecha de préstamo, por defecto ahora
        self.fecha_devolucion = fecha_devolucion  # Fecha de devolución
        self.fecha_devuelto = fecha_devuelto  # Fecha en que se devolvió el libro
        self.cantidad_solicitada = cantidad_solicitada  # Cantidad de libros solicitados

    @staticmethod  # Indica que este método no necesita acceso a la instancia
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo):
        # Método para sumar días laborales a una fecha
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)  # Agrega un día
            # Verifica si el día es laboral (lunes a viernes) y no es un festivo
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1  # Incrementa el contador de días laborales
        return fecha_prestamo  # Devuelve la nueva fecha

    def calcular_fechas(self):
        # Método para calcular las fechas de préstamo y devolución
        if self.ejemplares_disponibles > 0:  # Verifica si hay ejemplares disponibles
            if self.ejemplares_disponibles >= self.cantidad_solicitada:  # Verifica si se pueden prestar los libros solicitados
                self.fecha_prestamo = datetime.now()  # Establece la fecha de préstamo a ahora
                # Calcula la fecha de devolución sumando días laborales
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)  # Suma 5 días laborales