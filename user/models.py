from django.db import models
from translation.models import Language
from django.contrib.auth.models import User


class LangSession(models.Model):
    session=models.CharField(max_length=50)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.session
    
class UserDetail(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    userInfo = models.TextField(max_length=300)
    fb_url = models.URLField(max_length=100, blank=True, null=True)
    tw_url = models.URLField(max_length=100, blank=True, null=True)
    gg_url = models.URLField(max_length=100, blank=True, null=True)
    ln_url = models.URLField(max_length=100, blank=True, null=True)
    pi_url = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.username)