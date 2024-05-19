from django.forms import ModelForm

from users.models import User

class UserForm(ModelForm):
    """Form for the User model."""
    
    class Meta:
        model = User
        fields = [
            'email',
        ]