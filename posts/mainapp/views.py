from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView

from .models import *

from .forms import CommentForm


class PostListView(ListView):

    model = Post
    template_name = 'mainapp/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'mainapp/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request.POST or None)
        return context


class CommentCreateView(CreateView):
    pass
    # form_class = CommentForm
    #
    # def form_valid(self, form):
    #     new_comment = form.save(commit=False)
    #     post = Post.objects.get(slug=self.kwargs['slug'])
    #     author = User.objects.get(pk=self.request.user.pk)
    #     new_comment.author = author
    #     new_comment.related_post = post
    #     new_comment.save()
    #     post.comments.add(new_comment)
    #     return HttpResponseRedirect('post')



