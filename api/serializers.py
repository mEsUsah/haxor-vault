from rest_framework import serializers
from vault.models import App, AppType, Credential
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = ['id','name']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id','name', 'apptype','user']


class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id','name', 'apptype','user','credentials']

    credentials = serializers.SerializerMethodField()

    def get_credentials(self, object):
        credentials = object.credential_set.all()
        serializer = CredentialSerializer(credentials, many=True)
        return serializer.data


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id','app','username','password']


class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id','app','username','password']

    app = serializers.SerializerMethodField()

    def get_app(self, object):
        app = object.app
        serializer = AppSerializer(app)
        return serializer.data