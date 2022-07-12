from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_details = models.CharField(max_length=150)
    book_author = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='bookpics')
    book_path = models.FileField(upload_to='bookpath/')

    def __str__(self):
        return self.book_name










    
