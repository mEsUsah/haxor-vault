from rest_framework import serializers
from vault.models import App, AppType
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AppTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppType
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id','name', 'apptype','user']