from django.db.models import fields
import profiles
from rest_framework import serializers 
from .models import offer, offerCategorie,offerSkills,Skill

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = offer


class OfferSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = offerSkills
        # ['id', 'offerTitle', 'offerCategory', 'salary', 'location','offerType','experience','skills','description']



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Skill


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = offerCategorie
