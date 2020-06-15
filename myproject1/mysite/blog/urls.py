
from django.urls import path, re_path
from blog import views

app_name='blog'
urlpatterns = [

    path('', views.PostLV.as_view(), name='index'),

    path('post/', views.PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Examplearchive/: /2012/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    path('archive/today/',  views.PostTAV.as_view(), name='post_today_archive'),
]
