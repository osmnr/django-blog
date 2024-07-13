from django.db import models
from translation.models import Language
from django.contrib.auth.models import User


class LangSession(models.Model):
    session=models.CharField(max_length=50)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.session
    
class UserDetail(models.Model):
    username = models.OneToOneField(User, related_name='user_detail', on_delete=models.CASCADE)
    userInfo = models.TextField(blank=True, null=True)
    fb_url = models.URLField(max_length=100, blank=True, null=True)
    tw_url = models.URLField(max_length=100, blank=True, null=True)
    gg_url = models.URLField(max_length=100, blank=True, null=True)
    ln_url = models.URLField(max_length=100, blank=True, null=True)
    pi_url = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.username)
    

class Log(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    requestHeaders = models.TextField()
    responseHeaders = models.TextField()
    getParams = models.TextField(null=True, blank=True)
    postData = models.TextField(null=True, blank=True)
    senderIP = models.GenericIPAddressField()
    userAgent = models.CharField(max_length=255)
    statusCode = models.IntegerField()
    responseContent = models.TextField()
    responseTime = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.method} {self.path} - {self.statusCode}'