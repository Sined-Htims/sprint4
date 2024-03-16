import datetime

from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post


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
    context = {'post_list': post_list}
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
