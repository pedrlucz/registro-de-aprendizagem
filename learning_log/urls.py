from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')) # a home, a principal, pra ele ir pra esse arquivo que fica dentro do app
]


