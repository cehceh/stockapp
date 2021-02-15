from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return 'user: {}, email: {}'.format(self.username, self.email)