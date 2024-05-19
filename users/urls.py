from django.urls import path
from users.views import user

urlpatterns = [
    path("login",  user.login, name="login"),
    path("logout",  user.logout, name="logout"),
    path("register",  user.register, name="register"),
    path("verify/<str:id>",  user.verify, name="verify"),
]