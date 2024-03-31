# Importo las librerias necesarias
import pandas as pd
import os # para utilizar os.system("cls") para limpiar la consola

# Creo la clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

# Creo la funcion crear_libro, esta solicita al usuario los campos requeridos para instanciar la clase Libro, y luego lo agrega a la lista lista_libros
def crear_libro():
    os.system("cls")
    titulo = input("Ingrese el título\n").upper()
    autor = input("\nIngrese el autor\n").upper()
    genero = input("\nIngrese el género\n").upper()
    puntuacion = input("\nIngrese la puntuación\n") # pasar a float y validar entrada
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)

# Creo la funcion ordenar_generos, esta hace un set con los generos de la lista_libros y los devuelve como una lista ordenada
def ordenar_generos():
    generos = set()
    for libro in lista_libros:
        generos.add(libro.genero)
    generos_ordenados = sorted(list(generos))
    return generos_ordenados

# Creo la funcion buscar_libros, esta solicita al usuario el genero a buscar y devuelve una lista filtrada con los libros de dicho genero
def buscar_libros():
    generos_ordenados = ordenar_generos()
    genero_seleccionado = ()
    while genero_seleccionado not in generos_ordenados:
        os.system("cls")
        print("Seleccione el género del libro que desea buscar.\n\nLas opciones disponibles son:\n")
        print(generos_ordenados)
        genero_seleccionado = input().upper()
    libros_filtrados = list(filter(lambda x: x.genero == genero_seleccionado, lista_libros))
    os.system("cls")
    print(f"Libros de {genero_seleccionado}:\n")
    for libro in libros_filtrados:
        print(f"* {libro.titulo}")
    input("\nPresione cualquier tecla para continuar...\n")

# Creo la funcion recomendar_libros, esta solicita al usuario un genero y devuelve el libro mejor puntuado de dicho genero
def recomendar_libros():
    generos_ordenados = ordenar_generos()
    genero_seleccionado = ()
    while genero_seleccionado not in generos_ordenados:
        os.system("cls")
        print("¿Que género es de su interés?\n\nLas opciones disponibles son:\n")
        print(generos_ordenados)
        genero_seleccionado = input().upper()
    libros_filtrados = list(filter(lambda x: x.genero == genero_seleccionado, lista_libros))
    max = 0
    for libro in libros_filtrados:
        if float(libro.puntuacion) > max:
            mejor_puntuado = libro
            max = float(libro.puntuacion)
    os.system("cls")
    print(f"""El libro mejor calificado dentro del género {genero_seleccionado} es:\n\n"{mejor_puntuado.titulo}, por {mejor_puntuado.autor} con una calificación de {mejor_puntuado.puntuacion}""")
    input("\nPresione cualquier tecla para continuar...\n")

lista_libros = []

# Importo la base de libros desde un archivo CSV
ruta = "C:/Users/fwaib/OneDrive/Escritorio/ISTEA/1_2 MINERIA DE DATOS 1/mineria_de_datos_1/tp2_recomendacion_de_libros/recomendacion_de_libros.csv" # aca pego la ruta del archivo
origen_csv = pd.read_csv(ruta) # importo el archivo CSV a un dataframe de Pandas
lista_importada = origen_csv.values.tolist()
for fila in lista_importada:
    titulo = fila[0].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    autor = fila[1].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    genero = fila[2].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    puntuacion = float(fila[3])
    libro_importado_nuevo = Libro(titulo, autor, genero, puntuacion) # instancio la clase
    lista_libros.append(libro_importado_nuevo)

# main
while True:
    os.system("cls")
    print("BIENVENIDOS AL SISTEMA DE RECOMENDACION DE LIBROS.\n\nSeleccione una opción:\n\nA para agregar un libro.\nB para buscar libros por género.\nR para recomendar un libro.\nS para salir.\n")
    seleccion = input().upper()
    if seleccion == "A":
        crear_libro()
    elif seleccion == "B":
        buscar_libros()
    elif seleccion == "R":
        recomendar_libros()
    elif seleccion == "S":
        os.system("cls")
        print("Adios")
        break
    else:
        os.system("cls")
        print("Opción inválida. Por favor intente nuevamente.\n")
        input("Presione cualquier tecla para continuar...\n")
