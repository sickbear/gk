# coding=utf-8
from django import template
from django.utils.safestring import mark_safe
from ..models import TemplateFragment, SiteLogo

register = template.Library()


@register.simple_tag()
def cms_template(name):
    """Вставка html-шаблонов из базы."""
    template = TemplateFragment.objects.get(name=name)
    return mark_safe(template.text)


@register.simple_tag()
def logo():
    """Вставка логотипа сайта."""
    logotype = SiteLogo.objects.all()[0]
    return logotype.logo
