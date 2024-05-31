from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = Movie
        fields = '__all__'
