import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encodings='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'a',encodings='utf8') as archivo:
            print('Catalogo de Peliculas'.center(50,'-'))
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')