from django.db import models
import uuid

from vault.models import AppType
from users.models import User

class App(models.Model):
    id = models.UUIDField(default=uuid.uuid4, 
                          unique=True, 
                          primary_key=True, 
                          editable=False)
    name = models.CharField(max_length=250, blank=True, null=True)
    apptype = models.ForeignKey(AppType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']