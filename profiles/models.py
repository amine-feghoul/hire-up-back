from email.policy import default
from django.contrib.postgres.fields import ArrayField
from authapp.models import userAccount
from django.db import models
from common.models import Language, contractType, studyField,offerType

from common.models import Position,companyType,Sector,Skill,Institute,Degree
def uploadProfilePic(instance,filename):
    return '/'.join(['profile_pictures/',str(instance.user_id_id)+"/" ,filename])
def uploadCompayLogo(instance,filename):
    return '/'.join(['company_logos/',str(instance.user_id_id)+"/" ,filename])
def uploadAgencyLogo(instance,filename):
    return '/'.join(['agency_logos/',str(instance.user_id_id)+"/" ,filename])
# Create your models here.

class authorizedViewers(models.Model):
    user = models.ForeignKey(userAccount,to_field='id',on_delete=models.CASCADE,related_name="user_id")
    viewer = models.ForeignKey(userAccount,to_field='id',on_delete=models.CASCADE,related_name="viewer_id")



class profileModel(models.Model):
    user = models.ForeignKey(userAccount,to_field='id',related_name="profile", on_delete=models.CASCADE,unique=True)
    fullName = models.CharField(max_length=250,default="")
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=16,default="")
    phone = models.CharField(max_length = 12,default="") 
    profilePic = models.ImageField(blank=True,upload_to = uploadProfilePic )
    bio = models.TextField(default="")
    salary = models.IntegerField(default=0  )
    position = models.ForeignKey(Position,to_field='label',on_delete=models.CASCADE,default="position")
    yearsOfExperience = models.IntegerField(default=0)
    experienceInPosition = models.IntegerField(default=0)
    linkedin = models.URLField(default="")
    #education
    def __str__(self):
        return self.fullName


class WishedPosition(models.Model):
    position = models.ForeignKey(Position,to_field='label',on_delete=models.CASCADE,default="position")
    contractType = models.ForeignKey(contractType,to_field="label",on_delete=models.CASCADE)
    jobType = models.ForeignKey(offerType,to_field="label",on_delete=models.CASCADE)
    def __str__(self):
        return self.position

class userSkill(models.Model):
    user = models.ForeignKey(userAccount,to_field="id",on_delete = models.CASCADE)
    label = models.ForeignKey(Skill,to_field="label",on_delete=models.CASCADE,default = "")
    
    def __str__(self):
        return self.label.label
    
class SkillsWhichedForPosition(models.Model):
    user = models.ForeignKey(userAccount,to_field="id",on_delete=models.CASCADE)
    skill = models.ForeignKey(userSkill,to_field="id",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.skill.label



class Education(models.Model):
    user = models.ForeignKey(userAccount,to_field="id",on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree,to_field="label",on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute,to_field="label",on_delete=models.CASCADE,default="")
    field = models.ForeignKey(studyField,to_field="label",on_delete=models.CASCADE,default="")
    description = models.CharField(max_length=1000,default='')
    startDate = models.DateField()
    endDate = models.DateField(blank=True,null=True)
    isOngoing = models.BooleanField(default=False)
    def __str__(self):
        return self.degree.label


class userLanguage(models.Model):
    user = models.ForeignKey(userAccount,to_field="id",on_delete = models.CASCADE)
    label = models.ForeignKey(Language,to_field="label",on_delete=models.CASCADE,default = "")
    def __str__(self):
        return self.label.label


class Experience(models.Model):
    #job_category = models.ForeignKey(Degrees,to_field="degree")
    user = models.ForeignKey(userAccount,to_field="id",on_delete=models.CASCADE)
    company = models.CharField(max_length=250,default="")
    title = models.ForeignKey(Position,to_field="label",on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(blank=True,null=True)
    isOngoing = models.BooleanField(default=False)
    description = models.TextField(default="")
    def __str__(self):
        return self.title.label

class RecruiterProfile(models.Model):
    user  = models.ForeignKey(userAccount,to_field='id', on_delete=models.CASCADE)
    fullName = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    companyAddress = models.CharField(max_length=255)
    phone = models.CharField(max_length = 12,default="")    
    sector =  models.ForeignKey(Sector,to_field="label",on_delete=models.CASCADE,default = "Info & Tech")
    webSite = models.URLField(blank=True)
    # profilePic = models.ImageField(blank=True)
    # companyLogo = models.ImageField(blank=True,upload_to = uploadCompayLogo)
    companyType = models.ForeignKey(companyType,to_field="label",on_delete=models.CASCADE,default = "Start-up")
    # agency_logo = models.ImageField()
    employees=models.IntegerField(default=1)
    companyDescription = models.TextField(default="")
    def __str__(self):
        return self.fullName
    def get_id(self):
        return self.id

class AgencyProfile(models.Model):
    user  = models.ForeignKey(userAccount,to_field='id', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField( max_length=150)
    address = models.CharField(max_length=255)
    agencyName = models.CharField(max_length=255)
    agencyAddress = models.CharField(max_length=255)
    phone = models.CharField(max_length = 12,default="")    
    # agency_logo = models.ImageField(blank=True,upload_to = uploadAgencyLogo)
    def __str__(self):
        return self.agencyName

