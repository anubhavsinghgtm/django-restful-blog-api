from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=255,default='a')
    meta_description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        if(self.slug != 'a'):
            original_slug = self.slug
        else:
            original_slug = slugify(self.title)
        unique_slug = original_slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{num}"
            num += 1
        return unique_slug