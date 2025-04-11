# books/models.py
from django.db import models
from django.urls import reverse

class Publication(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publications = models.ManyToManyField(Publication)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.id])