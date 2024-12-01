from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ("title", "publication_year", "author")
  def validate_publication_year(self, value):
    current_year = date.today().year
    if value > current_year:
      raise serializers.ValidationError("Publication year cannot be in the future")
    return value
    
class AuthorSerializer(serializers.ModelSerializer):
  book = BookSerializer(many=True, read_only=True)
  class Meta:
    model = Author
    fields = ("name", "book")
    """
    we have book and author serializer the author serializer conatins the book serialzer 
    the book serializer contains validate publication year which contrils the year of the book not to be in the future
    """