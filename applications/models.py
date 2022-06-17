from django.db import models
from authapp.models import userAccount
from offers.models import offer
from profiles.models import profileModel
# Create your models here.
class applicationState(models.Model):
    state = models.CharField(max_length=150,default="on_hold",unique=True)
    def __str__(self):
        return self.state

class applications(models.Model):
    candidate = models.ForeignKey(profileModel,to_field="id",on_delete=models.CASCADE,related_name="applicantion_owner")
    offer = models.ForeignKey(offer,to_field="id",on_delete=models.CASCADE,default=0,related_name="offer_id")
    employer = models.ForeignKey(userAccount,to_field="id",on_delete=models.CASCADE,default=0,related_name="offer_owner")
    state = models.ForeignKey(applicationState,default="on_hold",to_field="state",on_delete=models.SET_DEFAULT)


