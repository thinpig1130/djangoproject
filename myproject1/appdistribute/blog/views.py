from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView

from blog.models import Post


#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

#--- DetailView
class PostDV(DetailView):
    model = Post


#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    date_field = 'modify_dt'
    paginate_by = 5

class PostYAV(YearArchiveView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    date_field = 'modify_dt'
    make_object_list = True
    paginate_by = 5

class PostMAV(MonthArchiveView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    date_field = 'modify_dt'
    # make_object_list = True
    paginate_by = 5


class PostDAV(DayArchiveView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    date_field = 'modify_dt'
    paginate_by = 5



