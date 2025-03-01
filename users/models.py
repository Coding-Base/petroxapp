from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    # Add related_name to avoid conflict
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid conflict with default 'auth.User.groups'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Avoid conflict with default 'auth.User.user_permissions'
        blank=True
    )

    def __str__(self):
        return self.username


