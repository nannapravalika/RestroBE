from django.db import models

# Create your models here.

class UserRegModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=100)
    user_mobile=models.BigIntegerField()
    user_password=models.CharField(max_length=100)
    
    class Meta:
        db_table='user_registration_details'
        
        