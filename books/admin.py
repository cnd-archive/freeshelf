from books.models import Book, Category
from django.contrib import admin

class CategoryInline(admin.StackedInline):
    model = Category.books.through

class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'book_url', 'author', 'author_url', 'description', 'cover']
    inlines = [CategoryInline,]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'slug']

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
