from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Función para crear paginación
def get_paginated_movies(request, movies, page_number):
    # Divide en página de 10 películas
    paginator = Paginator(movies, page_number)
    page_number = request.query_params.get('page', 1)

    try:
        # Obtener la página solicitada
        movies_page = paginator.page(page_number)

    except PageNotAnInteger:
        # Número de página no es un entero
        movies_page = paginator.page(1)

    except EmptyPage:
        # Página fuera del rango
        movies_page = paginator.page(paginator.num_pages)
    
    return movies_page