from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    categoryName = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.categoryName


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)
    #    if not self.slug:
    #        self.slug = f"{slugify(self.title)}-{self.id}"
    #        unique_slag = self.slug
    #        num = 1
    #        while BlogPost.objects.filter(slug=unique_slag).exists():
    #            unique_slag = f"{self.slug}-{num}"
    #            num += 1
    #        self.slug = unique_slag
    #        super().save(*args, **kwargs)



