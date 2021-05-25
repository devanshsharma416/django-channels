from django.contrib import admin
from .models import Article, Publication

# Register your models here.

admin.site.register(Publication)
admin.site.register(Article)

