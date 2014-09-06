from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

import models
import serializer

class BacheViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Bache.objects.all()
    serializer_class = serializer.BacheSerializer
