from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)