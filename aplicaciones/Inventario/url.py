from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarObjeto/', views.registrarObjeto),
    path('edicionObjeto/<codigo>', views.edicionObjeto),
    path('editarObjeto/', views.editarObjeto),
    path('eliminarObjeto/<codigo>', views.eliminarObjeto),
]