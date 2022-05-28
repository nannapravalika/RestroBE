from django.shortcuts import render,redirect,get_object_or_404
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
    user=request.session["user_id"]
    use=UserRegModel.objects.filter(user_id=user)
    user=UserRegModel.objects.filter(user_id=user).first()
    res=RestaurentRegModel.objects.filter(status="Accepted")
    if request.method=="POST":
        date=request.POST.get("date")
        time=request.POST.get("time")
        restaurent_name=request.POST.get("restaurant")
        table_category=request.POST.get("table")
        members=request.POST.get("members")
        srequest=request.POST.get("srequest")
        
        
        UserBookTableModel.objects.create(user=user,date=date,time=time,restaurent_name=restaurent_name,table_category=table_category,members=members,request=srequest)
   
    req=RestaurentRegModel.objects.filter(status="Accepted")
    
    return render(request,'customer/customer-dashboard.html',{'req':req,"res":res, "user":use})

def user_profile(request):
    userr=request.session["user_id"]
    user=UserRegModel.objects.filter(user_id=userr)
    use=get_object_or_404(UserRegModel,user_id=userr)
    if request.method=="POST":
        user_name=request.POST.get("name")
        user_email=request.POST.get("email")
        user_mobile=request.POST.get("mobile")
         
        use.user_name=user_name
        use.user_email=user_email
        use.user_mobile=user_mobile
         
        use.save(update_fields=["user_name","user_email","user_mobile","user_password"])
        
        
         
        
    return render(request,'customer/customer-my-profile.html',{'user':user})

def user_feedback(request,id):
    userr=request.session["user_id"]
    use=UserRegModel.objects.filter(user_id=userr)
    
    user=UserBookTableModel.objects.filter(booking_id=id)
    if request.method=="POST":
        message=request.POST.get("message")
        rate=request.POST.get("star")
        user_reg=UserRegModel.objects.filter(user_id=userr).first()
        user_booking=UserBookTableModel.objects.filter(booking_id=id).first()
        user_restaurent=RestaurentRegModel.objects.filter(restaurent_id=id)
        
        
        UserFeedbackModel.objects.create(user=user_reg,feedback=message,rating=rate,user_booking=user_booking)
    
    
    return render(request,'customer/customer-give-feedback.html',{"user":user,"user":use})

def user_view_orders(request):
    return render(request,'customer/customer-my-orders-view.html')

def user_book_table_res(request,id):
    req=RestaurentRegModel.objects.filter(restaurent_id=id)
    table=RestaurentTableModel.objects.filter(restaurent=id)
    
    return render(request,'customer/customer-order-food.html',{'req':req,'table':table})

def user_view_bookings(request):
    user=request.session["user_id"]
    user=UserBookTableModel.objects.filter(user=user)
     
    return render(request,'customer/customer-view-booking-status.html',{"user":user})

def user_payment(request,id):
    user=UserBookTableModel.objects.filter(booking_id=id)
    return render(request,'customer/customer-payment.html',{"user":user})

def user_restaurent_select(request):
    res=RestaurentRegModel.objects.filter(status="Accepted")
    return render(request,'customer/customer-restaurent-select.html',{'res':res})

def user_book_table(request,id):
    user=request.session["user_id"]
    use=UserRegModel.objects.filter(user_id=user)
    res=RestaurentTableModel.objects.filter(table_id=id)
    if request.method=="POST":
        date=request.POST.get("date")
        time=request.POST.get("time")
        restaurent_name=request.POST.get("restaurant")
        table_category=request.POST.get("table")
        members=request.POST.get("members")
        srequest=request.POST.get("srequest")
        user=UserRegModel.objects.filter(user_id=user).first()
        user_table=RestaurentTableModel.objects.filter(table_id=id).first()
        restaurent = RestaurentRegModel.objects.get(restaurent_name=restaurent_name)
         
        price = 0
        hotel_table_price = RestaurentTableModel.objects.get(table_id=id)
        if members=='0-2':
            price = int(hotel_table_price.table_price) 
        if members=='2-4':
            price = int(hotel_table_price.table_price) * 2
        if members=='4-8':
            price = int(hotel_table_price.table_price) * 3
        if members=='8-10':
            price = int(hotel_table_price.table_price) * 4
        if members=='10+':
            price = int(hotel_table_price.table_price) * 5        
        
        print('********',price)
        print(restaurent)
        user_restaurent = restaurent.restaurent_id
        print(user_restaurent)
         
        UserBookTableModel.objects.create(price=price,user_restaurent=restaurent,user_table=user_table,user=user,date=date,time=time,restaurent_name=restaurent_name,table_category=table_category,members=members,request=srequest)
        messages.success(request, "Sucessfully Booked the Table" )
    return render(request,'customer/customer-table-booking.html',{"res":res, "user":use})

def user_view_menu(request):
    return render(request,'customer/customer-view-menu.html')



