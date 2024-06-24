from django.db import models

class SiteConfig(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.key



class Navigation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=False)
    is_external = models.BooleanField(default=False)


    def __str__(self):
        return self.name


