from django.shortcuts import render_to_response, get_object_or_404
from books.models import Category, Book

def home(request):
    books = Book.objects.all()
    return render_to_response('index.html', {'books': books})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = category.books.all()
    return render_to_response('category.html', {'category': category, 'books': books})
