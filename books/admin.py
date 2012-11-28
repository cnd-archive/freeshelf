from books.models import Book, Category
from django.contrib import admin
from imagekit.admin import AdminThumbnail

class CategoryInline(admin.StackedInline):
    model = Category.books.through

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'book_url',
            'free', 'print_url', 'publish_year']}),
        ('Author', {'fields': ['author', 'author_url']}),
        ('Display', {'fields': ['description', 'cover']}),
    ]
    inlines = [CategoryInline,]
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'slug', 'subtitle', 'banner']

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
