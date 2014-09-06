from django.forms import widgets
from rest_framework import serializers
import models


class BacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bache
        fields = ('id', 'latitud', 'longitud', 'tipo_marcador')

        #fields = ('id', 'latitud', 'longitud', 'usuario', 'tipo_marcador')
        #read_only_fields = ('usuario',)
