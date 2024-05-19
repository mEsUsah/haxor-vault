from django.urls import path
from api.views import apptypes, apps, credentials

urlpatterns = [
    path('v1/apptypes', apptypes.list),
    
    path('v1/apps', apps.list),
    path('v1/apps/<str:id>', apps.details),
    path('v1/apps/<str:id>/delete', apps.delete),

    path('v1/credentials', credentials.list),
    path('v1/credentials/<str:id>', credentials.details),
    path('v1/credentials/<str:id>/delete', credentials.delete),
]