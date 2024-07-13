from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserDetail
from blog.models import BlogPost

@receiver(post_save, sender=User)
def createUserDetail(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(username=instance)

@receiver(post_save, sender=User)  
def saveUserDetail(sender, instance, **kwargs):
    instance.user_detail.save() 


@receiver(post_delete, sender=BlogPost)
def printNotification(sender, instance, **kwargs):
    print("\n\n Bir post silindi!. \n\n\n")
    
