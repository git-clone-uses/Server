from django.contrib import admin
from .models import *

class Data_Admin(admin.ModelAdmin):
    
    list_display = [field.name for field in Incoming_Data._meta.fields]
    list_filter = ("IMEI", "Type_of_Message")
    
class Obj_Admin(admin.ModelAdmin):
    
    list_display = [field.name for field in Object._meta.fields]

admin.site.register(Incoming_Data, Data_Admin)
admin.site.register(Object, Obj_Admin)