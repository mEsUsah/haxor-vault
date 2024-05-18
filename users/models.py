import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password_hash = models.CharField(max_length=200, blank=True, null=True)
    verification_code = models.UUIDField(
        default=uuid.uuid4, 
        unique=True)