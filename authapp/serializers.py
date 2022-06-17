from django.db import models
from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from authapp.models import userAccount, userType
from profiles.models import profileModel
from profiles.serializers import ProfileSerializer,appProfileSerializer
user = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model= user
        fields = ['id','email','name','password',"user_type"]


class userAccountSerializer(serializers.ModelSerializer):
    
    # profile = ProfileSerializer(read_only = True)
    class Meta:
        model = userAccount
        fields = "__all__"
        
        
class userTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = userType
        fields = "__all__"