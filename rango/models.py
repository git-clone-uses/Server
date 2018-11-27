from django.db import models
from . import serv


# Create your models here.
class Incoming_Data(models.Model):
    id = models.AutoField(primary_key=True)
    Type_of_Message = models.CharField(max_length = 3, default = "NA")
    IMEI = models.CharField(max_length = 256, default = "NA")
    data = models.CharField(max_length = 256, default = "NA")
    time = models.CharField(max_length = 256, default = "NA")
    server_date_time = models.CharField(max_length = 30, default = "NA")
    lat = models.CharField(max_length = 256, default = "NA")
    lot = models.CharField(max_length = 256, default = "NA")
    speed = models.CharField(max_length = 256, default = "NA")
    course = models.CharField(max_length = 256, default = "NA")
    height = models.CharField(max_length = 256, default = "NA")
    sats = models.CharField(max_length = 256, default = "NA")
    hdops = models.CharField(max_length = 256, default = "NA")
    inputs = models.CharField(max_length = 256, default = "NA")
    outputs = models.CharField(max_length = 256, default = "NA")
    adc = models.CharField(max_length = 256, default = "NA")
    ibutton = models.CharField(max_length = 256, default = "NA")
    params = models.CharField(max_length = 256, default = "NA")
    
    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Incoming Data"

        
        
class Object(models.Model):
    id = models.AutoField(primary_key = True)
    IMEI = models.CharField(max_length = 20, unique = True)
    Gos_Nomer = models.CharField(max_length = 9)
    Description = models.CharField(max_length = 156, default = "NA")
    
    