# coding=utf-8
from django import forms
from .models import Thread, Post, Category, Section


class PostForm(forms.ModelForm):
    """Форма комментария."""

    class Meta:
        model = Post
        exclude = ['user', 'user_ip', 'thread', 'date_created', 'last_updated']


class ThreadForm(forms.ModelForm):
    """Форма темы."""

    class Meta:
        model = Thread
        exclude = ['section', 'user', 'posts_count', 'last_updated']


class ThreadPageForm(forms.ModelForm):
    """Форма темы с выбором категории и раздела."""
    qs = Category.objects.filter(is_hidden=False, sections_count__gt=0)
    category = forms.ModelChoiceField(queryset=qs, empty_label=None)
    section = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(ThreadPageForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update(
            {
                'class': 'progect-input',
                'id': 'category',
                'required': ''
            }
        )
        self.fields['section'].widget.attrs.update(
            {
                'class': 'progect-input',
                'id': 'section',
                'required': ''
            }
        )

    class Meta:
        model = Thread
        exclude = ['section', 'user', 'posts_count', 'last_updated']

