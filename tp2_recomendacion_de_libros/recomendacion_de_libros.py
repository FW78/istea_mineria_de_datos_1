import pandas as pd
import os # importo os para utilizar os.system("cls") para limpiar la consola

# Creo la clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

# Importo la base de libros desde un archivo CSV
ruta = "C:/Users/fwaib/OneDrive/Escritorio/ISTEA/1_2 MINERIA DE DATOS 1/mineria_de_datos_1/tp2_recomendacion_de_libros/recomendacion_libros.csv" # aca pego la ruta del archivo
origen_csv = pd.read_csv(ruta) # importo el archivo CSV a un dataframe de Pandas
lista_importada = origen_csv.values.tolist()
for fila in lista_importada:
    titulo = fila[0].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    autor = fila[1].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    genero = fila[2].strip().upper().replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U")
    puntuacion = float(fila[3])
    libro_importado_nuevo = Libro(titulo, autor, genero, puntuacion) # instancio la clase
    lista_libros.append(libro_importado_nuevo)

# Igreso al loop principal
opciones = ["A", "B", "R", "E"]
seleccion = ()

while seleccion not in opciones:
    os.system("cls")
    print("Bienvenidos al sistema de recomendación de libros. \n Seleccione una opción: \n A para agregar un libro. \n B para buscar libros por género. \n R para recomendar un libro. \n E para salir.")
    seleccion = input().upper()
    if seleccion == "A":
        os.system("cls")
        titulo = input("Ingrese el título \n").upper()
        autor = input("Ingrese el autor \n").upper()
        genero = input("Ingrese el género \n").upper()
        puntuacion = input("Ingrese la puntuación \n") # pasar a int y validar entrada
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)
        seleccion = ()
    elif seleccion == "B":
        generos = set()
        for libro in lista_libros:
            generos.add(libro.genero)
        generos_ordenados = sorted(list(generos))
        os.system("cls")
        print("Seleccione el género del libro que desea buscar.\n\nLas opciones disponibles son:\n")
        print(generos_ordenados)
        genero_seleccionado = input().upper()
        libros_filtrados = list(filter(lambda x: x.genero == genero_seleccionado, lista_libros))
        os.system("cls")
        print(f"Libros de {genero_seleccionado}:\n")
        for libro in libros_filtrados:
            print(f"* {libro.titulo}")
        input("\n Presione cualquier tecla para continuar\n")
        seleccion = ()
    elif seleccion == "R":
        generos = set()
        for libro in lista_libros:
            generos.add(libro.genero)
        generos_ordenados = sorted(list(generos))
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
        print(f"""El libro mejor calificado dentro del género {genero_seleccionado} es:\n\n "{mejor_puntuado.titulo}, por {mejor_puntuado.autor} con una calificación de {mejor_puntuado.puntuacion}""")
        input("\n Presione cualquier tecla para continuar\n")
        seleccion = ()
    elif seleccion == "E":
        os.system("cls")
        print("Adios")