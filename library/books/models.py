from django.db import models

# Create your models here.

    
class Author(models.Model):
    authorid = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    age = models.CharField(max_length = 10)
    country = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name
    
class Book(models.Model):
    isbn = models.CharField(max_length = 20)
    title = models.CharField(max_length = 100)
    authorid = models.CharField(max_length = 20)
    author = models.ForeignKey(Author)
    publisher = models.CharField(max_length = 50)
    publishdate = models.DateField()
    price = models.CharField(max_length = 10)
    def __unicode__(self):
        return self.title