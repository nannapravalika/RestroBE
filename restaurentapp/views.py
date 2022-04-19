from urllib import request
from django.shortcuts import render

# Create your views here.
def restro_reg(request):
    return render(request,'restaurants/restaurant-register.html')
    
def restro_login(request):
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

