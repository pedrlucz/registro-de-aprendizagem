from django.urls import path
from . import views # da mesma pasta que eu to, eu quero importar tal coisa, o .

urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics', views.topics, name = 'topics'),
    path('topic/<topic_id>/', views.topic, name = 'topic'), # dentro do // o tópico que eu quero ver, o que eu colocar dentro do <> vai ser uma variável
]


