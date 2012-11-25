from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_url = models.CharField(max_length=255)
    author_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers")
    thumbnail = ImageSpecField(
        [ResizeToFit(width=200, height=200, upscale=False)],
        image_field='cover', format='JPEG', options={'quality': 90})
    added_at = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.added_at:
            self.added_at = timezone.now()
        super(Book, self).save()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Category, self).save()
