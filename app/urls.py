from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
        path('envios/', views.ver_envios, name='ver_envios'),
]
