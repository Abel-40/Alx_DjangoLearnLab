from django.db import models

class Book(models.Model):
 title = models.CharField( max_length=200,null = True,blank = True)
 author = models.CharField(max_length=100,null = True,blank = True)
 publication_year =models.IntegerField(null = True,blank = True)
