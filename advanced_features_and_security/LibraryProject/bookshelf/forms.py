# bookshelf/forms.py
from django import forms
from .models import Book  # Import the Book model

# Model form for Book
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Link the form to the Book model
        fields = ['title', 'description']  # Include the fields you want in the form

