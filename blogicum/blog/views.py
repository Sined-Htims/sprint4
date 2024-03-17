import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from blog.models import Category, Post
from blog.forms import PostForm


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=datetime.datetime.now()
    )[:5]  # only
    context = {'page_obj': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'category',
            'author',
        ).filter(
            pub_date__lt=datetime.datetime.now(),
            is_published=True,
            category__is_published=True
        ),  # only
        pk=id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.values(
            'title',
            'description',
            'slug',
            'is_published',
        ).filter(is_published=True),
        slug=category_slug
    )
    post_list = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        category__slug=category_slug,
        pub_date__lt=datetime.datetime.now()
    )  # only
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)


class ProfileDetailView(DetailView):
    model = User
    template_name = 'blog/profile_detail.html'
    # Пришлось задавать в явном виде т.к. после переопределения get_object
    # он начал тригерится на шаблон auth/user_detail.html

    def get_object(self):
        pass
        # чтобы использовать слаг для url с профилем. Перерыл множество информации


class PostsCreateViews(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_form.html'
    success_url = 'blog:profile_detail'
