from django.db import models
from restaurentapp.models import RestaurentRegModel,RestaurentTableModel

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
    user_restaurent=models.ForeignKey(RestaurentRegModel,db_column="user_restaurent",on_delete=models.CASCADE,null=True)
    user_table=models.ForeignKey(RestaurentTableModel,db_column="user_table",on_delete=models.CASCADE,null=True)
    date=models.DateField(max_length=100)
    time=models.TimeField()
    restaurent_name=models.CharField(max_length=100)
    table_category=models.CharField(max_length=100)
    members=models.CharField(max_length=100)
    request=models.TextField()
    status=models.CharField(default="pending",max_length=100)    
    
    class Meta:
        db_table='user_booking_details'  
        
class UserFeedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserRegModel,db_column="user",on_delete=models.CASCADE) 
    user_restaurent=models.ForeignKey(RestaurentRegModel,db_column="user_restaurent",on_delete=models.CASCADE,null=True)
    user_table=models.ForeignKey(RestaurentTableModel,db_column="user_table",on_delete=models.CASCADE,null=True)
    user_booking=models.ForeignKey(UserBookTableModel,db_column="user_booking",on_delete=models.CASCADE)
    rating=models.CharField(max_length=100)
    feedback=models.TextField()
    date=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='user_feedback' 
    
    
    
            