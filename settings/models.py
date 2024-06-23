from django.db import models

class SiteConfig(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.key

