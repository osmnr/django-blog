from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    is_selectable = models.BooleanField(default='False')

    def __str__(self):
        return self.name


class TranslationKey(models.Model):
    key = models.CharField(unique=True, max_length=255)
    
    def __str__(self):
        return self.key


class Translation(models.Model):
    key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
    value = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.key)
        
    class Meta:
        unique_together = ('key', 'language',)

