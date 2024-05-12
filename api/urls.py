from django.urls import path
from . import views

urlpatterns = [
    path('v1/apptypes', views.apptype_list),
    
    path('v1/apps', views.app_list),
    path('v1/apps/<str:id>', views.app_details),
    path('v1/apps/<str:id>/delete', views.app_delete),

    path('v1/credentials', views.credential_list),
    path('v1/credentials/<str:id>', views.credential_details),
    path('v1/credentials/<str:id>/delete', views.credential_delete),
]