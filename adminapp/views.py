from django.shortcuts import render,redirect

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
    return render(request,'admin/admin-view-requests.html')

def admin_view_restaurants(request):
    return render(request,'admin/admin-view-restaurants.html')

def admin_view_restaurant_menu(request):
    return render(request,'admin/admin-view-restaurant-menu.html')

def admin_view_orders(request):
    return render(request,'admin/admin-view-orders.html')



