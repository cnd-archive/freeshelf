from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from books.models import Category, Book
from books.forms import BookSuggestionForm


def custom_404(request):
    categories = Category.objects.order_by('name').all()
    return render_to_response('404.html',
        {'categories': categories},
        context_instance=RequestContext(request))


def home(request):
    books = Book.for_free.order_by('-added_at').all()
    categories = Category.objects.order_by('name').all()
    return render_to_response('index.html',
        {'books': books, 'categories': categories},
        context_instance=RequestContext(request))


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.order_by('name').all()
    books = category.books.filter(free=True).order_by('-added_at').all()
    return render_to_response('category.html',
        {'category': category, 'books': books, 'categories': categories},
        context_instance=RequestContext(request))


def suggest(request):
    if request.method == 'POST':
        form = BookSuggestionForm(request.POST)
        if form.is_valid():
            request.flash['success'] = \
                "Thanks for your suggestion. We'll check it out and " + \
                "hopefully add it to FreeShelf soon."
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = BookSuggestionForm() # An unbound form

    return render_to_response('suggest.html',
        {'form': form},
        context_instance=RequestContext(request))
