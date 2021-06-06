from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


import uuid # for profile slugs
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save # signal for profile creation
# from django.contrib.auth.models import AbstractUser # import base user model for profile
from django.dispatch import receiver 
from allauth.account.signals import user_signed_up

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.username)


class UserProfile(models.Model):   # 'accounts.CustomUser'
    user         = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address      = models.CharField(max_length=150, blank=True, null=True)
    birth_date   = models.DateField(default=now, blank=True, null=True)
    age          = models.CharField(max_length=150, blank=True, null=True)
    city         = models.CharField(max_length=60, default="",  blank=True, null=True)
    photo        = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    profile_uuid = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4,
        editable=False,
        unique=True
    ) # to use as a "slug" for profiles

    # def __str__(self):
    #    return self.user.first_name
    def __str__(self):
        return f'Profile for user {self.user.username}'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    # @receiver(post_save, sender=CustomUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.save()
