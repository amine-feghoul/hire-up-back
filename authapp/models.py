
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager

class userType(models.Model):
    type = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.type

class UserAccountManager(BaseUserManager):
    def create_user(self,email,name,user_type,password=None):
        if not email:
            raise ValueError("user must have an eamil")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.user_type = userType.objects.get(type=user_type)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self,email,name,password=None):
        if not email:
            raise ValueError("user must have an eamil")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.user_type = userType.objects.get(type="admin")
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class userAccount(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_type = models.ForeignKey(userType,to_field='type',on_delete=models.CASCADE,default="condidate")
    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['name','user_type']

    def get_name(self):
        return self.name


    def get_id(self):
        return self.id

    
    def get_email(self):
        return self.email

    def get_user_type(self):
        return self.user_type
