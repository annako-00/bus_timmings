from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

     
class Route(models.Model):
     route=models.CharField(max_length=100,primary_key=True)




class Busprofile(models.Model):
     
     bno=models.CharField(max_length=100,primary_key=True)
     bname=models.CharField(max_length=100,null=True)
     username=models.CharField(max_length=50)
     
     bio=models.CharField(max_length=100,null=True)
     phno=models.IntegerField()

     ststopname=models.CharField(max_length=100,null=True)
     ststoptime=models.CharField(max_length=100,null=True)

     stop2name=models.CharField(max_length=100,null=True)
     stop2time=models.CharField(max_length=100,null=True)


     stop3name=models.CharField(max_length=100,null=True)   
     stop3time=models.CharField(max_length=100,null=True)

     stop4name=models.CharField(max_length=100,null=True)
     stop4time=models.CharField(max_length=100,null=True)

     stop5name=models.CharField(max_length=100,null=True)   
     stop5time=models.CharField(max_length=100,null=True)

     stop6name=models.CharField(max_length=100,null=True)   
     stop6time=models.CharField(max_length=100,null=True)


     endstopname=models.CharField(max_length=100,null=True) 
     endstoptime=models.CharField(max_length=100,null=True)  

     def __str__(self):
          return self.bname  
     

     
class Updates(models.Model):
     busname=models.CharField(max_length=50)
     busno=models.CharField(max_length=50)
     update=models.TextField(max_length=200)

     def __str__(self):
          return self.busname   



class Stopname(models.Model):
      
     brname=models.ForeignKey(Busprofile,on_delete=models.CASCADE,null=True)
     routename=models.ForeignKey(Route,on_delete=models.CASCADE,null=True)
     stopname=models.CharField(max_length=100,null=True)
     stoptime=models.CharField(max_length=100,null=True)

      

      
     