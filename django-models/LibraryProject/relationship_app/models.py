from django.db import models

class Author(models.Model):
  name = models.CharField(max_length = 100)
  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length =100)
  author = models.ForeignKey(Author , on_delete = models.CASCADE)
  def __str__(self):
    return self.title
  class Meta:
    permissions = [
      ("can_add_book"),
      ("can_change_book"),
      ("can_delete_book"),
    ]

class Library(models.Model):
  name = models.CharField(max_length = 100)
  book = models.ManyToManyField(Book)
  def __str__(self):  
    return self.name
class Librarian(models.Model):
  name = models.CharField(max_length = 100)
  library = models.OneToOneField(Library, on_delete = models.CASCADE)
  def __self__(self):
    return self.name



























# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# Signal to automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to save the UserProfile whenever the User model is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()









# class UserProfile(models.Model):
#   ADMIN ='Admin'
#   LIBRARIAN = 'Librarian'
#   MEMBER='Member'

#   Roles = [
#     (ADMIN,'Admin'),
#     (LIBRARIAN,'Librarian'),
#     (MEMBER,'Member')
#   ]
#   role = models.CharField(max_length = 100,choices=Roles,default=MEMBER)
#   user = models.OneToOneField('auth.User', on_delete = models.CASCADE)
#   def __str__(self):
#     return f"{self.user} - {self.role}"