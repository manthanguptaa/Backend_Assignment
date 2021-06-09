import string
from django.db import models
from django.contrib.auth.models import User
import random 
from django.utils.text import slugify

def generate_slug():
    chars = string.ascii_lowercase + string.digits
    size=10
    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
class book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    publish_date = models.DateTimeField()
    summary = models.CharField(max_length=500)
    content = models.CharField(max_length=3000)
    cover_book_photo = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=50)
    
    def __str__(self):
        return self.book_name

    def save(self, *args, **kwargs):
        self.slug = generate_slug()
        super(book,self).save(*args, **kwargs)

    def book_slug(self):
        return slugify(self.book_name)+'-'+self.slug
