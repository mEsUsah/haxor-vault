import os
from dotenv import load_dotenv
from django.contrib import admin
from django.urls import path, include

load_dotenv(override=True)
DEBUG = os.getenv("DEBUG", 'False').lower() in ('true', '1', 't')

urlpatterns = [
    path('jwt/', include('jwtauth.urls')),
    path('api/', include('api.urls')),
    path('', include('users.urls')),
    path('', include('vault.urls')),
]

# Only enable the admin interface in DEBUG mode
if DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + urlpatterns
