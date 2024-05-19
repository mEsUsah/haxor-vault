from django.contrib.auth.backends import BaseBackend
from users.models import User


class AuthBackend(BaseBackend):
    """Custom authentication backend.
    
    Allows for authentication using the password_hash field.
    
    This allows for client side hashing of passwords.
    """
    
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        if user.password_hash == password:
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None