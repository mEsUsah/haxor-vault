from django.db import models
import uuid
from vault.models import App

class Credential(models.Model):
    id = models.UUIDField(default=uuid.uuid4, 
                          unique=True, 
                          primary_key=True, 
                          editable=False)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)