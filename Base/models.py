from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


###########################################
#              Category Model             #
###########################################

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



###########################################
#               Tag Model                 #
###########################################

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



###########################################
#              BlogPost Model             #
###########################################


class BlogPost(models.Model):

    class BlogPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(published=True)
        
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=255,default='a')
    featured_image = models.ImageField(upload_to='BlogImages/', blank=True, null=True)
    meta_description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    objects = models.Manager()                # default manager
    postObject = BlogPostObjects()            # custom manager


    ####### to return the title 
    def __str__(self):
        return self.title

    ###### to save the unique slug 
    def save(self, *args, **kwargs):
        self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    ##### to generate the unique slug
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