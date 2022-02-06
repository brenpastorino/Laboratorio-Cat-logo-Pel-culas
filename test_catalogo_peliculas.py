from dominio.pelicula import Película
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    try:
        print('''Opciones:
        1.Agregar película
        2.Listar películas
        3.Eliminar catálogo de películas
        4.Salir''')
        opcion = int(input(f'Escribe tu opción (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Película(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Salimos del programa...')


