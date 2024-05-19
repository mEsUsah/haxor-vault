from django.forms import ModelForm

from vault.models import App, Credential

class AppForm(ModelForm):
    """Form for the App model."""
    
    class Meta:
        model = App
        fields = [
            'name',
            'apptype'
        ]

class CredentialForm(ModelForm):
    """Form for the Credential model."""
    
    class Meta:
        model = Credential
        fields = [
            'app',
            'username',
            'password',
        ]