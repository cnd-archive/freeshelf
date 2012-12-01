from django.shortcuts import render_to_response, get_object_or_404
from django import template
from django.conf import settings
from books.models import Category, Book

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


def home(request):
    books = Book.for_free.order_by('-added_at').all()
    categories = Category.objects.order_by('name').all()
    return render_to_response('index.html',
        {'books': books, 'categories': categories})


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.order_by('name').all()
    books = category.books.filter(free=True).order_by('-added_at').all()
    return render_to_response('category.html',
        {'category': category, 'books': books, 'categories': categories})
