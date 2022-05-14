from django.shortcuts import render,redirect,get_object_or_404
from restaurentapp.models import *
# Create your views here.
 
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        print(name)
        if name =='admin' and password =='admin':
            return redirect ('admin_dashboard')
        else :
            print ('invalid')  
    return render(request,'admin/admin-login.html')

def admin_dashboard(request):
    return render(request,'admin/admin-dashboard.html')

def admin_feedback(request):
    return render(request,'admin/admin-feedback.html')

def admin_view_bookings(request):
    return render(request,'admin/admin-view-bookings.html')

def admin_view_customers(request):
    return render(request,'admin/admin-view-customers.html')

def admin_view_requests(request):
    req=RestaurentRegModel.objects.all()
    return render(request,'admin/admin-view-requests.html',{'req':req})

def accept_restaurant(request,id):
    obj=get_object_or_404(RestaurentRegModel,restaurent_id=id)
    obj.status="Accepted"
    obj.save(update_fields=["status"])
    return redirect("admin_view_requests")

def reject_restaurant(request,id):
    obj=get_object_or_404(RestaurentRegModel,restaurent_id=id)
    obj.status="Rejected"
    obj.save(update_fields=["status"])
    return redirect("admin_view_requests")

def admin_view_restaurants(request):
    req=RestaurentRegModel.objects.all()
    return render(request,'admin/admin-view-restaurants.html',{'req':req})

def admin_view_restaurant_menu(request):
    return render(request,'admin/admin-view-restaurant-menu.html')

def admin_view_orders(request):
    return render(request,'admin/admin-view-orders.html')



