
from django.contrib import admin
from django.urls import path, include
from pythonbasic.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

]
