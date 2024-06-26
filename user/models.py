from django.db import models
from translation.models import Language

class LangSession(models.Model):
    session=models.CharField(max_length=50)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.session