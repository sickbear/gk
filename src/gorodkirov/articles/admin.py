# coding: utf-8
from django.db import models
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from mptt.admin import MPTTModelAdmin
from tinymce.widgets import TinyMCE
from tinymce import HTMLField
from .models import Rubric, Article, InformationType, ArticleType, Tag, Author


@register(InformationType)
class InformationTypeAdmin(MaterialModelAdmin):
    """Админка для типов информации."""
    list_display = ('id', 'name')
    icon_name = 'perm_media'


@register(ArticleType)
class InformationTypeAdmin(MaterialModelAdmin):
    """Админка для типов статей."""
    list_display = ('id', 'name')
    icon_name = 'art_track'


@register(Tag)
class TagAdmin(MaterialModelAdmin):
    """Админка для тегов."""
    list_display = ('id', 'text')
    search_fields = ('text', )
    icon_name = 'label'


@register(Rubric)
class InformationTypeAdmin(MaterialModelAdmin):
    """Древовидная админка для рубрик."""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}
    icon_name = 'dashboard'


@register(Article)
class ArticleAdmin(MaterialModelAdmin):
    """Админка для статей."""
    list_display = ('title', 'id', 'rubric', 'is_published', 'author', 'published_at', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug', 'id', 'author__name')
    filter_horizontal = ('tags',)
    icon_name = 'description'

    formfield_overrides = {
        HTMLField: {
            'widget': TinyMCE()
        }
    }


@register(Author)
class AuthorAdmin(MaterialModelAdmin):
    """Админка для авторов."""
    icon_name = 'assignment_ind'
