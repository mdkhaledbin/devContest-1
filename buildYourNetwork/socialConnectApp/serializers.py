from rest_framework import serializers
from .models import User

class userRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': "Passwords don't match."})
        return data
    
    def create(self, validateData):
        validateData.pop('password2')
        user = User.objects.create_user(**validateData)
        return user