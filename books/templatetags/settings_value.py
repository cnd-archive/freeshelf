from django import template
from django.conf import settings

register = template.Library()

@register.filter
def setting(value):
    return getattr(settings, value, "")
