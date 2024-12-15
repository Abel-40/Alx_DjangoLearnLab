from django.contrib import admin
from .models import Post

admin.site.register(Post) # we register our posts so that it can be managed by django admin built in interface

