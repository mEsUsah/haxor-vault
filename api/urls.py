from django.urls import path
from . import views

urlpatterns = [
    path('v1/apps/', views.app_index),
    path('v1/apps/create', views.app_create),
    path('v1/apps/<str:app_id>', views.app),
]