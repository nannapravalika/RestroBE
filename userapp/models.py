from django.db import models
from restaurentapp.models import *

# Create your models here.

class UserRegModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=100)
    user_mobile=models.BigIntegerField()
    user_password=models.CharField(max_length=100)
    
    class Meta:
        db_table='user_registration_details'
        
class UserBookTableModel(models.Model):
    booking_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserRegModel,db_column="user",on_delete=models.CASCADE)
    restaurent=models.ForeignKey(RestaurentRegModel,db_column="restaurent",on_delete=models.CASCADE)
    table=models.ForeignKey(RestaurentTableModel,db_column="table",on_delete=models.CASCADE)
    
    
          