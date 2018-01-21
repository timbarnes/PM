from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from tinymce import models as tinymce_models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                parent_link=True)
    picture = models.ImageField(upload_to='media/profilepics/', blank=True)
    home = models.CharField(max_length=100, blank=True)
    interests = models.CharField(max_length=200, blank=True)
    objectives = models.CharField(max_length=200, blank=True)
    joined = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=10, blank=True)
    bio = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        print("Account created.")
    instance.account.save()
