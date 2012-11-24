from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_url = models.CharField(max_length=255)
    author_url = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers")
    added_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.title
