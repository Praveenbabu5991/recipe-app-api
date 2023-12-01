from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """serializer for the user model"""
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

        extra_kwargs={
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email':{'required': True,'allow_blank':False},
            'password': {'required': True,'allow_blank':False,'min_length':5},
            }


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user model"""
    # resume=serializers.CharField(source='userprofile.resume')
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']


