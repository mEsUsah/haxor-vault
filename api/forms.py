from django.forms import ModelForm

from vault.models import App, Credential

class AppForm(ModelForm):
    class Meta:
        model = App
        fields = [
            'name',
            'apptype'
        ]

class CredentialForm(ModelForm):
    class Meta:
        model = Credential
        fields = [
            'app',
            'username',
            'password',
        ]