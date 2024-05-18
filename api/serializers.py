from rest_framework import serializers
from vault.models import App, AppType, Credential

class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = ['id','name']


class AppsSerializer(serializers.ModelSerializer):
    """
    Serializer for apps. Does NOT include related credentials
    """

    class Meta:
        model = App
        fields = ['id','name', 'apptype','user']

    apptype = serializers.SerializerMethodField()
    def get_apptype(self, object):
        apptype = object.apptype
        serializer = AppTypeSerializer(apptype)
        return serializer.data


class AppSerializer(serializers.ModelSerializer):
    """
    Serializer for apps used to show related credentials on app
    """

    class Meta:
        model = App
        fields = ['id','name', 'apptype','user','credentials']

    credentials = serializers.SerializerMethodField()
    def get_credentials(self, object):
        credentials = object.credential_set.all()
        serializer = CredentialsSerializer(credentials, many=True)
        return serializer.data
    
    apptype = serializers.SerializerMethodField()
    def get_apptype(self, object):
        apptype = object.apptype
        serializer = AppTypeSerializer(apptype)
        return serializer.data


class CredentialsSerializer(serializers.ModelSerializer):
    """
    Serializer for credentials. Does NOT include related app details
    """
    class Meta:
        model = Credential
        fields = ['id','app','username','password']


class CredentialSerializer(serializers.ModelSerializer):
    """
    Serializer for credentials used to show related app details
    """
    class Meta:
        model = Credential
        fields = ['id','app','username','password']

    app = serializers.SerializerMethodField()

    def get_app(self, object):
        app = object.app
        serializer = AppsSerializer(app)
        return serializer.data