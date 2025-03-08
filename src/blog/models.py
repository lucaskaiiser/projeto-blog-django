from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=True)
    content = models.TextField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    

class Post(models.Model):

    class CustomManager(models.Manager):
        def get_published(self):
            return self.filter(is_published=True).order_by('-pk')
        
    objects:CustomManager = CustomManager()
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True
    )
    excert = models.CharField(max_length=255, default='')
    is_published = models.BooleanField(default=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/', blank=True, default='')
    cover_in_post = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, default='')
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='post_created_by'
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='post_updated_by'
    )

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        
        url_to_post = reverse('blog:post', args=(self.slug,))
        return url_to_post
        
    

    