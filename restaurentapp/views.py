from urllib import request
from django.shortcuts import render,redirect
from .models import RestaurentMenuModel,RestaurentRegModel
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
        name = request.POST.get('email')
        password =request.POST.get('Password')
        
        try:
           check=RestaurentRegModel.objects.get(restaurent_email=name,password=password)
           request.session["email"]=check.restaurent_email
           return redirect ('student_home')
        except: 
            messages.error(request, "Message sent." )
    return render(request,'restaurants/restaurant-login.html')

def restro_dashboard(request):
    return render(request,'restaurants/restaurant-dashboard.html')

def restro_add_menu(request):
    return render(request,'restaurants/restaurant-add-menu.html')

def restro_view_menu(request):
    return render (request,'restaurants/restaurant-view-menu.html')

def restro_edit_menu(request):
    return render (request,'restaurants/restaurant-edit.html')

def restro_view_table_bookings(request):
    return render (request,'restaurants/restaurant-view-booking-table.html')

def restro_view_feedback(request):
    return render (request,'restaurants/restaurant-view-feedback.html')

def restro_view_food_orders(request):
    return render (request,'restaurants/restaurant-view-orders-food.html')

