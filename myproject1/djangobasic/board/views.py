from django.views.generic import ListView, DetailView
from board.models import Post


#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'board/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5


#--- DetailView
class PostDV(DetailView):
    model = Post
