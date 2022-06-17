from django.db.models import fields
from rest_framework import serializers
from .models import Sector, companyType, profileModel,RecruiterProfile,AgencyProfile, userLanguage,userSkill,Education,Experience

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profileModel
        fields = '__all__'
       
class appProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = profileModel
            fields = ["id","user","address","salary","position","fullName","profilePic"]
            



class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = '__all__'

class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLanguage
        fields = ["label","id"]

class UserAddLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = userLanguage
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = ['companyName','companyAddress','companyDescription']


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyProfile
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSkill
        fields = '__all__'

class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyType
        fields = ['label']


class CompanySectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['label']
        
