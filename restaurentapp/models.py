from django.db import models

# Create your models here.
class RestaurentRegModel(models.Model):
    restaurent_id=models.AutoField(primary_key=True)
    restaurent_name=models.CharField(max_length=100)
    restaurent_email=models.EmailField(max_length=100)
    restaurent_mobile=models.BigIntegerField()
    restaurent_address=models.CharField(max_length=100)
    restaurent_logo=models.ImageField(upload_to='images/')
    restaurent_license=models.ImageField(upload_to='images/')
    restaurent_password=models.CharField(max_length=100)
    status=models.CharField(default="pending",max_length=100)
    
    class Meta:
        db_table='restaurent_registration_details'

class RestaurentMenuModel(models.Model):
    menu_id=models.AutoField(primary_key=True)
    restaurent=models.ForeignKey(RestaurentRegModel,db_column="restaurent",on_delete=models.CASCADE,related_name='restaurent')
    menu_food_type=models.CharField(max_length=100)
    menu_category=models.CharField(max_length=100)
    menu_name=models.CharField(max_length=100)
    menu_price=models.CharField(max_length=100)  
    menu_quantity=models.CharField(max_length=100)
    menu_details=models.CharField(max_length=100)
    menu_image=models.ImageField(upload_to='images/')
    
    class Meta:
        db_table='restaurent_menu_details'