from django.db.models import fields
from django.utils import tree
from rest_framework import serializers

from profiles.serializers import ProfileSerializer
from .models import applications
from authapp.serializers import UserCreateSerializer,userAccountSerializer
from profiles.serializers import appProfileSerializer,RecruiterSerializer
from offers.serializers import OffersSerializer
class ApplicationsSerializer(serializers.ModelSerializer):
    # condidate_id = ProfileSerializer(read_only=True)
    class Meta:
        model = applications
        fields=["id","candidate","offer","employer","state"]

        def create(self, validated_data):
            application = applications.objects.create(**validated_data)   
            return application

class readApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = applications
        fields=["id","candidate","offer","employer","state"]

       