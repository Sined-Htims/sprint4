from django.contrib import admin
from .models import Category, Location, Post

admin.site.register(Location)


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Модель категории для изменения в админ-зоне"""

    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'is_published',
        'slug',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Модель публикации для изменения в админ-зоне"""

    list_display = (
        'title',
        'is_published',
        'category',
        'author',
        'location',
        'created_at',
        'pub_date',
    )
    list_editable = (
        'is_published',
        'category',
    )
    list_filter = ('category',)
    search_fields = ('title',)
