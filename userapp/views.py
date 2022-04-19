from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request,'customer/customer-login.html')

def user_reg(request):
    return render(request,'customer/customer-register.html')

def user_dashboard(request):
    return render(request,'customer/customer-dashboard.html')

def user_profile(request):
    return render(request,'customer/customer-my-profile.html')

def user_feedback(request):
    return render(request,'customer/customer-give-feedback.html')

def user_view_orders(request):
    return render(request,'customer/customer-my-orders-view.html')

def user_order_food(request):
    return render(request,'customer/customer-order-food.html')

def user_view_bookings(request):
    return render(request,'customer/customer-view-booking-status.html')

def user_book_table(request):
    return render(request,'customer/customer-table-booking.html')

def user_view_menu(request):
    return render(request,'customer/customer-view-menu.html')



