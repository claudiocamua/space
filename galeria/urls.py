from django.urls import path
from galeria.views import index, imagenes

urlpatterns = [
    path('', index),
    path('imagenes/', imagenes),
]