from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follower, Blocked, Post, Like

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
    
    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        
        # Remove the password field from the response
        representation.pop('password', None)  # This will exclude the password field
        
        return representation
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class FolloweSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'follower', 'following']
        
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocked
        fields = ['id', 'blocker', 'blocked']
              
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content']
        