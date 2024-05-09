from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('app/create', views.create_app, name="create-app"),
]