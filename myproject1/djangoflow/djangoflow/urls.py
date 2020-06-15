from django.contrib import admin
from django.urls import path, include
from hello_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_django.urls')),
]