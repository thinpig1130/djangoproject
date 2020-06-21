from django.urls import path, re_path
from board import views

app_name = 'board'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('add/', views.PostCreateView.as_view(), name="add"),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),
]