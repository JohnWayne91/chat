from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView

from .models import *

from .forms import CommentForm, RegisterUserForm, SignInUserForm


class PostListView(ListView):

    model = Posts
    template_name = 'mainapp/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Posts
    template_name = 'mainapp/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request.POST or None)
        return context


class CommentCreateView(CreateView):
    pass


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/sign_up.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('posts')


class SignInUser(LoginView):
    form_class = SignInUserForm
    template_name = 'mainapp/sign_in.html'

    def get_success_url(self):
        return reverse_lazy('posts')


def logout_user(request):
    logout(request)
    return redirect('posts')
