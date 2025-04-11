# books/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Publication

def book_list(request):
    books = Book.objects.all()
    publications = Publication.objects.all()
    return render(request, 'books/list.html', 
                  {'books': books, 'publications': publications})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'book': book})