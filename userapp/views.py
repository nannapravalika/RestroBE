from django.shortcuts import render,redirect
from .models import *
from restaurentapp.models import *
from django.contrib import messages
# Create your views here.
def user_login(request):
    if request.method=="POST":
        print("valid")
        name = request.POST.get('email')
        password =request.POST.get('password')
        
        try:
           check=UserRegModel.objects.get(user_email=name,user_password=password)
           request.session["user_id"]=check.user_id
           return redirect ('user_dashboard')
        except: 
            messages.error(request, "Message sent." )
    return render(request,'customer/customer-login.html')

def user_reg(request):
    if request.method=="POST":
        
        user_name=request.POST.get("name")
        user_email=request.POST.get("email")
        user_mobile=request.POST.get("mobile")
        user_password=request.POST.get("password")
         
        
        UserRegModel.objects.create(user_name=user_name,user_email=user_email,user_mobile=user_mobile,user_password=user_password)
        messages.error(request, "Message sent." )
    return render(request,'customer/customer-register.html')

def user_dashboard(request):
    req=RestaurentRegModel.objects.filter(status="Accepted")
    
    return render(request,'customer/customer-dashboard.html',{'req':req})

def user_profile(request):
    return render(request,'customer/customer-my-profile.html')

def user_feedback(request):
    return render(request,'customer/customer-give-feedback.html')

def user_view_orders(request):
    return render(request,'customer/customer-my-orders-view.html')

def user_book_table_res(request,id):
    req=RestaurentRegModel.objects.filter(restaurent_id=id)
    
    return render(request,'customer/customer-order-food.html',{'req':req})

def user_view_bookings(request):
    return render(request,'customer/customer-view-booking-status.html')

def user_book_table(request):
    res=RestaurentRegModel.objects.filter(status="Accepted")
    return render(request,'customer/customer-table-booking.html',{"res":res})

def user_view_menu(request):
    return render(request,'customer/customer-view-menu.html')



