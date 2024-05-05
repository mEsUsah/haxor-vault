from django.db import models
import uuid

class AppType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, 
                          unique=True, 
                          primary_key=True, 
                          editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name