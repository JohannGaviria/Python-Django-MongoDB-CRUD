from django.urls import path
from . import views


# URLs de la app de películas
urlpatterns = [
    path('gets', views.gets, name='gets'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('update/<int:movie_id>', views.update, name='update'),
    path('delete/<int:movie_id>', views.delete, name='delete'),
]
