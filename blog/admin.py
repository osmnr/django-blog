from django.contrib import admin
from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title','author')}

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)