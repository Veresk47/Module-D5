from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView , DetailView, CreateView, UpdateView, DeleteView,)
from .models import Author, Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/author.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news/post_detail.html'

class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    context_object_name = 'news'
    template_name = 'news/Post_list.html'
    paginate_by = 2


class PostSearch(ListView):
    model = Post
    ordering = 'dateCreation'
    context_object_name = 'news'
    template_name = 'news/Post_list_search.html'
    paginate_by = 2


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class NewsCreate( CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)



class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'



class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_list')
