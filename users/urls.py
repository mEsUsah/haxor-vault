from django.urls import path
from users.views import user

urlpatterns = [
    path("login",  user.session_start, name="login"),
    path("logout",  user.session_end, name="logout"),
    path("register",  user.register, name="register"),
    path("verify/<str:id>",  user.verify, name="verify"),
]