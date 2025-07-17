from django.urls import path
from . import views

urlpatterns = [
    path('notas/', views.listado_notas, name='listado_notas'),
]