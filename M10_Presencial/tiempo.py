# 1. Definir la clase Time y asignar atributos

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.normalize_time()  # Ajustar si hay exceso de segundos o minutos

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

# 2. Crear una función para sumar horas, minutos y segundos

    def normalize_time(self):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        self.hour = (total_seconds // 3600) % 24
        total_seconds %= 3600
        self.minute = total_seconds // 60
        self.second = total_seconds % 60

# 3. Modificar la clase Time para hacerla más robasta

    def increment_time(self, hour=0, minute=0, second=0):
        self.second += second
        self.minute += minute
        self.hour += hour
        self.normalize_time()


#  Funciones auxiliares

def time_to_int(time):
    """Convierte un objeto Time a segundos totales."""
    return time.hour * 3600 + time.minute * 60 + time.second


def int_to_time(seconds):
    """Convierte segundos totales a un nuevo objeto Time."""
    hours = (seconds // 3600) % 24
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return Time(hours, minutes, seconds)


def add_time(time, hours=0, minutes=0, seconds=0):
    """Suma una duración a un objeto Time y devuelve un nuevo objeto."""
    total_seconds = time_to_int(time)
    duration_seconds = hours * 3600 + minutes * 60 + seconds
    new_total = total_seconds + duration_seconds
    return int_to_time(new_total)


# Ejemplo de uso

mi_hora = Time(14, 30, 15)
print("Hora original:", mi_hora)

nueva_hora = add_time(mi_hora, 2, 45, 30)
print("Nueva hora (usando add_time):", nueva_hora)

mi_hora.increment_time(1, 90, 80)  # 1h 90m 80s = 2h 31m 20s
print("Hora después de increment_time:", mi_hora)

# 4. Clase propia de Jhon Regueros

class Fecha:
    # Listas con los días de la semana y los meses del año
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    def __init__(self, dia_semana="Lunes", dia_mes=1, mes=1):
        """Inicializa la fecha con día de la semana, día del mes y mes del año."""
        self.dia_semana = dia_semana
        self.dia_mes = dia_mes
        self.mes = mes
        self.validar_fecha()  # Verifica que los valores sean correctos

    def __str__(self):
        """Muestra la fecha en formato legible."""
        nombre_mes = self.meses[self.mes - 1]
        return f"{self.dia_semana}, {self.dia_mes} de {nombre_mes}"

    def validar_fecha(self):
        """Verifica que los valores estén dentro de rangos válidos."""
        if self.dia_semana not in self.dias_semana:
            raise ValueError(f"'{self.dia_semana}' no es un día laboral válido (solo lunes a viernes).")

        if not (1 <= self.mes <= 12):
            raise ValueError("El mes debe estar entre 1 y 12.")

        if not (1 <= self.dia_mes <= 31):
            raise ValueError("El día del mes debe estar entre 1 y 31.")

    def siguiente_dia(self):
        """Avanza al siguiente día laboral."""
        indice = self.dias_semana.index(self.dia_semana)
        if indice < 4:  # Si no es viernes
            self.dia_semana = self.dias_semana[indice + 1]
        else:
            # Si es viernes, reinicia a lunes y avanza el día del mes
            self.dia_semana = self.dias_semana[0]
            self.dia_mes += 1
            if self.dia_mes > 31:
                self.dia_mes = 1
                self.mes += 1
                if self.mes > 12:
                    self.mes = 1  # Reinicia el año

# Crear una fecha
mi_fecha = Fecha("Viernes", 31, 1)
print("Fecha actual:", mi_fecha)

# Avanzar al siguiente día
mi_fecha.siguiente_dia()
print("Siguiente día:", mi_fecha)

# Otra fecha
otra_fecha = Fecha("Martes", 15, 5)
print("Otra fecha:", otra_fecha)