from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('app/create', views.create_app, name="create-app"),
    path('app/<str:id>', views.edit_app, name="edit-app"),
    path('credential/create', views.create_credential, name="create-credential"),
    path('credential/<str:id>', views.edit_credential, name="edit-credential"),
]