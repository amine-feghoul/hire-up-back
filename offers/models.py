from django.db import models
from authapp.models import userAccount
from common.models import Skill,contractType,offerType
# Create your models here.

class offerCategorie(models.Model):
    label = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return str(self.category)

class experienceYears(models.Model):
    experience = models.CharField(max_length=250)
    def __str__(self):
        return str(self.experience)


class offer(models.Model): 
    userId = models.ForeignKey(userAccount,to_field="id",on_delete=models.CASCADE,default=0)
    category = models.ForeignKey(offerCategorie,to_field="label",on_delete=models.CASCADE,default="")
    companyProfile = models.ForeignKey("profiles.RecruiterProfile",to_field='id',on_delete=models.CASCADE,related_name="offer",default=1)
    title = models.CharField(max_length=255,default="")
    minSalary = models.IntegerField(default=0)
    maxSalary = models.IntegerField(default=0)
    location = models.CharField(max_length=255,default="")
    contractType = models.ForeignKey(contractType,to_field="label",on_delete=models.SET_DEFAULT,default="CDD")
    experience = models.IntegerField(default=0)
    description = models.TextField(default="")
    urgent = models.BooleanField(default=False)
    offerType = models.ForeignKey(offerType,to_field="label",on_delete=models.CASCADE,default="")
    createdAt = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_id(self):
        return self.id

    def get_userId(self):
        return self.userId


class offerSkills(models.Model):
    offer_id = models.ForeignKey(offer, to_field='id' ,on_delete=models.CASCADE)
    label = models.ForeignKey(Skill,to_field='label',on_delete =models.CASCADE,default="")

    def __str__(self):
        return self.label



    
