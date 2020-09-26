from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here
class User(auth.models.User, auth.models.PermissionsMixin):
    """
        Using auth user model for handling users
    """

    def __str__(self):
        return "@{}".format(self.username)
