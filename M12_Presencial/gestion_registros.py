"""Juntos: w = write/escribir o escribir, r = read/leer, A = appenda/anadir.
1. Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
2. Correr este codigo en su maquina local (que no tenga errores)
3. Verificar que se crea el archivo salida.txt, en el directorio actual, con sus datos.
"""

# w Funcion para escribir en el archivo

import csv

def escribirDocumento(data):
    with open("salida.txt", "a", encoding="utf-8") as fileToWriteTo:
        fileToWriteTo.write(data + "\n")


# TODO 1:
# Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.

miEntrada = 'Jhon,44,cena'
#escribirDocumento(miEntrada)

# TODO 2:
# a Despues de verificar el documento salida.txt, agregar 3 lineas con datos de companeros. 
def agregarAlDocumento(data):
    with open("salida.txt", "a", encoding="utf-8") as fileToWriteTo:
        fileToWriteTo.write(data + "\n")

    agregarAlDocumento("Sofia,30,almuerzo")
    agregarAlDocumento("Patricia,25,desayuno")
    agregarAlDocumento("Francisco,20,Cena")
        
# TODO 3: 
# r 

def leerDocumento():
    with open("salida.txt", "r", encoding="utf-8") as fileToReadFrom:
        contenido = fileToReadFrom.read()
        print("Contenido de salida.txt:\n")
        print(contenido)

leerDocumento()

# TODO 4:
# Cambiar capitulo13.py a un archivo de csv. Usarlo para que imprima solo los cantantes. 

with open("cantantes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "profesion"])
    writer.writeheader()
    cantantes = [
        "Luis Fonsi","Shakira","Los Del Río","Enrique Iglesias","Ricky Martin",
        "Juanes","Selena","Maná","Romeo Santos","Daddy Yankee","Gloria Estefan",
        "Marc Anthony","Carlos Vives","José Feliciano","Héctor Lavoe","Gipsy Kings",
        "Celia Cruz","Michel Teló","Thalía","Ricardo Montaner","Alejandro Sanz",
        "Juan Gabriel","Ritchie Valens","Aventura","J Balvin","Bad Bunny","RBD",
        "Salsa Kids","Rosalía","Soda Stereo","Los Bukis","Christina Aguilera",
        "Prince Royce","Carla Morrison","Maná","Julieta Venegas","La Oreja de Van Gogh",
        "Reik","Franco De Vita","Tito El Bambino","Don Omar","Kany García",
        "Vicente Fernández","Luis Miguel","Intocable","Sin Bandera","Chayanne",
        "Alejandro Fernández","Ha*Ash","Mon Laferte"
    ]
    for cantante in cantantes:
        writer.writerow({"nombre": cantante, "profesion": "cantante"})

print("\nCantantes en cantantes.csv:\n")
with open("cantantes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        if fila["profesion"] == "cantante":
            print(fila["nombre"])

#TODO 5:
# Crear codigo para hace otra cosa con el archiva .csv"""

contador = 0
with open("cantantes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        if fila["profesion"] == "cantante":
            contador += 1

print(f"\nNúmero total de cantantes: {contador}")
