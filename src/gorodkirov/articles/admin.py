# coding: utf-8
from django.db import models
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from mptt.admin import MPTTModelAdmin
from tinymce.widgets import TinyMCE
from tinymce import HTMLField
from .models import (
    Rubric, Article, InformationType, ArticleType, Tag, Author,
    OperationalArticle, CityDetails, ChronicleRubric, ChronicleArticle, TestDriveArticle
)


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
    search_fields = ('text',)
    icon_name = 'label'


@register(Rubric)
class InformationTypeAdmin(MaterialModelAdmin):
    """Древовидная админка для рубрик."""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    icon_name = 'dashboard'


@register(Article)
class ArticleAdmin(MaterialModelAdmin):
    """Админка для статей."""
    list_display = ('title', 'id', 'rubric', 'is_published', 'author', 'published_at', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug', 'id', 'author__name')
    icon_name = 'description'

    formfield_overrides = {
        HTMLField: {
            'widget': TinyMCE()
        }
    }


@register(Author)
class AuthorAdmin(MaterialModelAdmin):
    """Админка для авторов."""
    search_fields = ('name', )
    icon_name = 'assignment_ind'


@register(OperationalArticle)
class OperationalArticleAdmin(MaterialModelAdmin):
    """Админка для оперативных новостей."""
    raw_id_fields = ('article', )
    list_display = ('article', 'get_published_at_date', 'get_published_to_date')
    ordering = ('article__date_sort',)
    search_fields = ('article__title', 'id')


@register(CityDetails)
class CityDetailsAdmin(MaterialModelAdmin):
    """Админка для Городских новостей."""
    raw_id_fields = ('article',)
    list_display = ('article', 'get_info_type', 'placement_unit', 'get_published_at_date', 'get_published_to_date')
    search_fields = ('article__title', 'id')


@register(ChronicleRubric)
class ChronicleRubricAdmin(MaterialModelAdmin):
    """Админка для рубрик Хроники."""
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    icon_name = 'dashboard'


@register(ChronicleArticle)
class ChronicleArticleAdmin(MaterialModelAdmin):
    """Адмика для статей Хроники."""
    raw_id_fields = ('article',)
    list_display = ('article', 'topic')
    search_fields = ('article__title', 'id')


@register(TestDriveArticle)
class TestDriveArticleAdmin(MaterialModelAdmin):
    """Адмика для статей Тест-драйва."""
    raw_id_fields = ('article',)
    list_display = ('article', )
    search_fields = ('article__title', 'id')
