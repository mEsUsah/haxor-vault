from rest_framework import serializers
from vault.models import App, AppType, Credential

class AppTypeSerializer(serializers.ModelSerializer):
    """Serializer for app types."""
    
    class Meta:
        model = AppType
        fields = ['id','name']


class AppsSerializer(serializers.ModelSerializer):
    """Serializer for apps. 
    
    Does NOT include related credentials.
    """

    class Meta:
        model = App
        fields = ['id','name', 'apptype','user']

    apptype = serializers.SerializerMethodField()
    def get_apptype(self, object: App):
        apptype = object.apptype
        serializer = AppTypeSerializer(apptype)
        return serializer.data


class AppSerializer(serializers.ModelSerializer):
    """Serializer for apps. 
    
    Includes related credentials on app and app type.
    """

    class Meta:
        model = App
        fields = ['id','name', 'apptype','user','credentials']

    credentials = serializers.SerializerMethodField()
    def get_credentials(self, object: App):
        credentials = object.credential_set.all()
        serializer = CredentialsSerializer(credentials, many=True)
        return serializer.data
    
    apptype = serializers.SerializerMethodField()
    def get_apptype(self, object: App):
        apptype = object.apptype
        serializer = AppTypeSerializer(apptype)
        return serializer.data


class CredentialsSerializer(serializers.ModelSerializer):
    """Serializer for credentials. 
    
    Does NOT include related app details.
    """

    class Meta:
        model = Credential
        fields = ['id','app','username','password']


class CredentialSerializer(serializers.ModelSerializer):
    """Serializer for credentials. 
    
    Includes related app details.
    """

    class Meta:
        model = Credential
        fields = ['id','app','username','password']

    app = serializers.SerializerMethodField()
    def get_app(self, object):
        app = object.app
        serializer = AppsSerializer(app)
        return serializer.data