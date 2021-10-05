from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion =None

while opcion != 4:
    try:
        print('opciones: ')
        print('1. Agregar Peliculas')
        print('2. Listar Peliculas')
        print('3. Eliminar catalogo peliculas')
        print('4. Salir')
        opcion = int(input('escribe tu opcion (1-4): '))

        if opcion ==1:
            nombre_pelicula = input('proporciona nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion=None

else:
    print('Salimos del programa ')
