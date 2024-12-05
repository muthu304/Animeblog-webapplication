from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=100)
    rating = models.CharField()
    content = models.TextField()
    img_url = models.ImageField(null=True, upload_to="posts/images")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title


class aboutus(models.Model):
    content = models.TextField()

    