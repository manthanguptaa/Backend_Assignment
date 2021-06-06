from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    publish_date = models.DateTimeField()
    summary = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.book_name
