from django.db import models


# Definición del modelo Movie para representar las películas
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    genres = models.BinaryField()

    def __str__(self):
        return self.title
