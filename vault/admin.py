from django.contrib import admin
from .models import AppType, App, Credential

# Register your models here.
admin.site.register(App)
admin.site.register(Credential)