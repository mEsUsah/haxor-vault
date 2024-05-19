from django.urls import path
from vault.views import apps, credentials, articles

urlpatterns = [
    path('', articles.home, name="home"),
    
    path('dashboard', apps.list, name="dashboard"),
    path('app/create', apps.create, name="create-app"),
    path('app/<str:id>', apps.edit, name="edit-app"),
    
    path('credential/create', credentials.create, name="create-credential"),
    path('credential/<str:id>', credentials.edit, name="edit-credential"),
]