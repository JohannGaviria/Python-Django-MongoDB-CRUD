from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Movie
from .serializers import MovieSerializer
from .utils import get_paginated_movies


# Logica para obtener todas las películas
@api_view(['GET'])
def gets(request):
    #  Obtiene todas las películas
    movies = Movie.objects.all()
    
    # Obtiene la página solicitada de películas
    movies_page = get_paginated_movies(request, movies, 10)
    
    # Serializa los datos de la película
    serializer = MovieSerializer(movies_page, many=True)

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'Movies found successfully',
        'data': {
            'movies': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Logica para buscar una película
@api_view(['GET'])
def search(request):
    # Obtener el parámetro de búsqueda
    query = request.GET.get('query')

    # Comprueba que se proporcione un parámetro de búsqueda
    if not query:
        return Response({
            'status': 'error',
            'message': 'Incorrect search parameters'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Busca las películas que coincidan
    movies = Movie.objects.filter(
        Q(title__icontains=query),
    ).distinct()

    # No existe películas con el titulo
    if not movies:
        return Response({
            'status': 'error',
            'message': 'No movies found matching your search'
        }, status=status.HTTP_404_NOT_FOUND)

    # Serializa los datos de la película
    serializer = MovieSerializer(movies, many=True)

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'Movies found successfully',
        'data': {
            'movies': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Logica para crear una película
@api_view(['POST'])
def create(request):
    # Serializa los datos recibidos en la solicitud
    serializer = MovieSerializer(data=request.data)

    # Verifica los datos válidos
    if serializer.is_valid():
        # Guarda los datos de la película
        serializer.save()

        # Devuelve los datos
        return Response({
            'status': 'success',
            'message': 'Movie created successfully',
            'data': {
                'movie': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Devuelve los errores de validación
    return Response({
        'status': 'error',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Logica para actualizar la pelicula
@api_view(['PUT'])
def update(request, movie_id):
    # Obtiene la película por su ID
    movie = get_object_or_404(Movie, id=movie_id)

    # Serializa los datos de la película
    serializer = MovieSerializer(movie, data=request.data)

    # Verifica los datos válidos
    if serializer.is_valid():
        # Guarda los datos de la película
        serializer.save()

        # Devuelve los datos
        return Response({
            'status': 'success',
            'message': 'Movie updated successfully',
            'data': {
                'movie': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Devuelve los errores de validación
    return Response({
        'status': 'error',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Logica para eliminar la película
@api_view(['DELETE'])
def delete(request, movie_id):
    # Obtine la película por su ID
    movie = get_object_or_404(Movie, id=movie_id)

    # Elimina la película
    movie.delete()

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'Movie deleted successfully'
    }, status=status.HTTP_204_NO_CONTENT)
