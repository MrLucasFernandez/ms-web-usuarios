from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarUsuarios, name='usuarios'),
    path('detalle/<str:pk>',views.FiltrarUsuario, name='detalle'),
    path('crear', views.CrearUsuario, name="crear"),
    path('actualizar/<str:pk>/', views.ActualizarUsuario, name="actualizar"),
    path('eliminar/<str:pk>/', views.EliminarUsuario, name="eliminar"),
    ]