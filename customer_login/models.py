from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.

class CustomerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    contact=models.IntegerField(null=False,blank=False)
    gender=models.CharField(max_length=15,null=False,blank=False)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return "Message from -" + self.name
