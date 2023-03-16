from django.urls import path
from .import views

urlpatterns = [
    path("login/", views.logar, name='logar'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("logout/", views.logout, name='logout'),
]