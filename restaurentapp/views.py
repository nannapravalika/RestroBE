from urllib import request
from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import *
from userapp.models import UserBookTableModel, UserFeedbackModel, UserRegModel
from django.contrib import messages

# Create your views here.
def restro_reg(request):
    
    if request.method=="POST" and "rlogo" in request.FILES and request.FILES["rlicence"] :
        
        restaurent_name=request.POST.get("rname")
        restaurent_email=request.POST.get("remail")
        restaurent_mobile=request.POST.get("mobile")
        restaurent_address=request.POST.get("address")
        restaurent_password=request.POST.get("password")
        restaurent_logo=request.FILES["rlogo"]
        restaurent_license=request.FILES["rlicence"]
        
        RestaurentRegModel.objects.create(restaurent_name=restaurent_name,restaurent_email=restaurent_email,restaurent_mobile=restaurent_mobile,restaurent_address=restaurent_address,restaurent_password=restaurent_password,restaurent_logo=restaurent_logo,restaurent_license=restaurent_license)
        messages.error(request, "Message sent." )
        
    return render(request,'restaurants/restaurant-register.html')
    
def restro_login(request):
    if request.method=="POST":
        print("valid")
        name= request.POST.get('email')
        password=request.POST.get('password')
        
        try:
           check=RestaurentRegModel.objects.get(restaurent_email=name,restaurent_password=password)
           print("ok")
           request.session["restaurent_id"]=check.restaurent_id
           
           return redirect ('restro_dashboard')
        except: 
            messages.error(request, "Message sent." )
    return render(request,'restaurants/restaurant-login.html')

def restro_dashboard(request):
    return render(request,'restaurants/restaurant-dashboard.html')

def restro_add_menu(request):
    restaurent_id=request.session["restaurent_id"]
    if request.method=="POST" and request.FILES['table_image']:
        restaurent=RestaurentRegModel.objects.filter(restaurent_id=restaurent_id).first()
        table_type=request.POST.get("category")
        table_price=request.POST.get("price")
        table_details=request.POST.get("details")
        table_image=request.FILES['table_image']
        RestaurentTableModel.objects.create(restaurent=restaurent,table_type=table_type,table_price=table_price,table_details=table_details,table_image=table_image)
        messages.error(request, "Message sent." )
        
    return render(request,'restaurants/restaurant-add-menu.html')

def restro_view_menu(request):
    restaurent=request.session["restaurent_id"]
    table=RestaurentTableModel.objects.filter(restaurent=restaurent)
    count=UserBookTableModel.objects.filter(status="Booked").count()
    return render (request,'restaurants/restaurant-view-menu.html',{'table':table,'count':count})

def restro_edit_menu(request):
    return render (request,'restaurants/restaurant-edit.html')

def restro_view_table_bookings(request):
    user=UserBookTableModel.objects.all()
    return render (request,'restaurants/restaurant-view-booking-table.html',{"user":user})

def accept_booking(request,id):
    obj=get_object_or_404(UserBookTableModel,booking_id=id)
    obj.status="Payment Pending"
    obj.save(update_fields=["status"])
    return redirect("restro_view_table_bookings")

def reject_booking(request,id):
    obj=get_object_or_404(UserBookTableModel,booking_id=id)
    obj.status="Not Available"
    obj.save(update_fields=["status"])
    return redirect("restro_view_table_bookings")


def restro_view_feedback(request):
    restaurent=request.session["restaurent_id"]
    feed=UserFeedbackModel.objects.filter(user_restaurent=restaurent)
    return render (request,'restaurants/restaurant-view-feedback.html',{'feed':feed})

def restro_view_food_orders(request):
    return render (request,'restaurants/restaurant-view-orders-food.html')

