from django.urls import path
from . import views # da mesma pasta que eu to, eu quero importar tal coisa, o .

urlpatterns = [
    path('', views.index),
]


