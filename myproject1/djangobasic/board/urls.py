from django.urls import path, re_path
from board import views

app_name = 'board'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    re_path(r'(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
]