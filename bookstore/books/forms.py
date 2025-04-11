# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publications', 'cover_image']
        widgets = {
            'publications': forms.CheckboxSelectMultiple,
        }