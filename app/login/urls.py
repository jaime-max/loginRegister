from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('subir/', views.subir, name = 'subir'),
    path('logout/', views.exit, name = 'exit'),
    path('register/', views.register, name='register'),
]
