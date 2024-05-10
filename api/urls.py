from django.urls import path
from . import views

urlpatterns = [
    path('v1/apps', views.app_list),
    path('v1/apps/<str:app_id>', views.app_details),
]