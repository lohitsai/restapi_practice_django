from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title')
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)