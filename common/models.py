from django.db import models

# Create your models here.

class Position(models.Model):
      label = models.CharField(max_length=150,unique=True)
      def __str__(self):
          return self.label


class Institute(models.Model):
      label = models.CharField(max_length=150,unique=True)
      def __str__(self):
          return self.label

class Degree(models.Model):
      label = models.CharField(max_length=150,unique=True)
      def __str__(self):
          return self.label

class companyType(models.Model):
    label = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.label

class Language(models.Model):
    label = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.label

class Sector(models.Model):
    label = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.label

class Skill(models.Model):
    label = models.CharField(max_length=250,unique=True,default="")
    def __str__(self):
        return self.label

class contractType(models.Model):
    label = models.CharField(max_length=150,default ="",unique=True)

    def __str__(self):
        return self.label

        
class offerType(models.Model):
    label = models.CharField(max_length=150,default ="",unique=True)

    def __str__(self):
        return self.label

class Site(models.Model):
    label = models.CharField(max_length=150,default ="",unique=True)

    def __str__(self):
        return self.label
    
class Category(models.Model):
    label = models.CharField(max_length=150,default ="",unique=True)
    def __str__(self):
        return self.label

class studyField(models.Model):
    label = models.CharField(max_length=150,default ="",unique=True)
    def __str__(self):
        return self.label