# books/admin.py
from django.contrib import admin
from .models import Book, Publication

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    list_filter = ['publications']
    search_fields = ['title', 'author']

admin.site.register(Book, BookAdmin)
admin.site.register(Publication)