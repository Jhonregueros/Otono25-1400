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