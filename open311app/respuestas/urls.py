from django.urls import path

from . import views

urlpatterns = [
    path('', views.respuestas, name='respuestas'),
]
