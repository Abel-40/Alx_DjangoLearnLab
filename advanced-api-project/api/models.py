from django.db import models

"""
author model that specifies name of the author 
we also have book model that have title ,author and publication year
auhtor and book have one to many relationship
"""
class Author(models.Model):
  name = models.CharField(max_length=100)
  

  def __str__(self):
    return self.name
class Book(models.Model): 
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  publication_year = models.IntegerField()
  def __str__(self):  
    return self.title
