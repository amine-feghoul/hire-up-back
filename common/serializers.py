from .models import Language, Site, Skill,Sector,companyType,offerType,Position,contractType,Degree,Institute, studyField
from rest_framework import serializers 

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Skill

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Sector

class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = companyType

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Language

class OfferTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = offerType

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Position

class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = contractType

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Degree

class InstituteSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ["label"]
        model = Institute

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = Site

class StudyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["label"]
        model = studyField