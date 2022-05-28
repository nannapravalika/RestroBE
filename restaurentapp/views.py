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
        
        if RestaurentRegModel.objects.filter(restaurent_email=restaurent_email).exists():
            messages.error (request, "Email already exist")
        else:
            RestaurentRegModel.objects.create(restaurent_name=restaurent_name,restaurent_email=restaurent_email,restaurent_mobile=restaurent_mobile,restaurent_address=restaurent_address,restaurent_password=restaurent_password,restaurent_logo=restaurent_logo,restaurent_license=restaurent_license)
            messages.success(request, "Account created successful")
        
    return render(request,'restaurants/restaurant-register.html')
    
def restro_login(request):
    if request.method=="POST":
        print("valid")
        name= request.POST.get('email')
        password=request.POST.get('password')
        
        try:
           check=RestaurentRegModel.objects.get(restaurent_email=name,restaurent_password=password)
           request.session["restaurent_id"]=check.restaurent_id
           status=check.status
           if status=="Accepted":
                return redirect('restro_dashboard')    
           elif status=="Rejected":
                messages.error(request,'Your Request has been Rejected, So you cannot Login')  
           elif status=="pending":
                print("pending")
                messages.info(request,'Your Status is Pending, You Cannot Login Now')  
        except: 
              messages.warning(request,'Invalid Login')
         
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
        total_tables=request.POST.get("tables")
        table_members=request.POST.get("members")
        table_image=request.FILES['table_image']
        
       
        try:
            RestaurentTableModel.objects.get(table_type=table_type)
            messages.error(request, "Table Already Exists" ) 
        except:
            RestaurentTableModel.objects.create(total_tables=total_tables,table_members=table_members,restaurent=restaurent,table_type=table_type,table_price=table_price,table_details=table_details,table_image=table_image)
            messages.success(request, "Sucessfully Created the Table" )
        
    return render(request,'restaurants/restaurant-add-menu.html')

def restro_view_menu(request):
    restaurent=request.session["restaurent_id"]
    table1=RestaurentTableModel.objects.filter(restaurent=restaurent).filter(table_type="Booths")
    table2=RestaurentTableModel.objects.filter(restaurent=restaurent).filter(table_type="Two to Four Person Tables")
    table3=RestaurentTableModel.objects.filter(restaurent=restaurent).filter(table_type="Bar Height Table")
    table4=RestaurentTableModel.objects.filter(restaurent=restaurent).filter(table_type="Family Dinning Table")
    table5=RestaurentTableModel.objects.filter(restaurent=restaurent).filter(table_type="Outdoor Table")
    
    count1=UserBookTableModel.objects.filter(status="Booked").filter(table_category="Booths").count()
    count2=UserBookTableModel.objects.filter(status="Booked").filter(table_category="Two to Four Person Tables").count()
    count3=UserBookTableModel.objects.filter(status="Booked").filter(table_category="Bar Height Table").count()
    count4=UserBookTableModel.objects.filter(status="Booked").filter(table_category="Family Dinning Table").count()
    count5=UserBookTableModel.objects.filter(status="Booked").filter(table_category="Outdoor Table").count()
    return render (request,'restaurants/restaurant-view-menu.html',{'table1':table1,'table2':table2,'table3':table3,'table4':table4,'table5':table5,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5})

def restro_edit_menu(request,id):
    restaurent_id=request.session["restaurent_id"]
    table=RestaurentTableModel.objects.filter(table_id=id)
    profile=RestaurentTableModel.objects.filter(table_id=id)
    edit=get_object_or_404(RestaurentTableModel,table_id=id)
    if request.method=="POST":
        restaurent=RestaurentRegModel.objects.filter(restaurent_id=restaurent_id).first()
        table_type=request.POST.get("category")
        table_price=request.POST.get("price")
        table_details=request.POST.get("details")
        total_tables=request.POST.get("tables")
        table_members=request.POST.get("members")
        
        if len(request.FILES)!=0:
            table_image=request.FILES['table_image']
            print(table_image)
            edit.restaurent=restaurent
            edit.table_type=table_type
            edit.table_price=table_price
            edit.table_details=table_details
            edit.total_tables=total_tables
            edit.table_members=table_members
            edit.table_image=table_image
            edit.save(update_fields=['restaurent','table_type','table_price','table_details','total_tables','table_members','table_image'])
            messages.success(request, "Sucessfully Updated the Table" )
        else:
            table_image=profile
            print(table_image)
            edit.restaurent=restaurent
            edit.table_type=table_type
            edit.table_price=table_price
            edit.table_details=table_details
            edit.total_tables=total_tables
            edit.table_members=table_members
            edit.table_image=table_image
            edit.save(update_fields=['restaurent','table_type','table_price','table_details','total_tables','table_members'])
            messages.success(request, "Sucessfully Updated the Table" )
            
    return render (request,'restaurants/restaurant-edit.html',{'table':table})

def restro_view_table_bookings(request):
    user=UserBookTableModel.objects.all()
    return render (request,'restaurants/restaurant-view-booking-table.html',{"user":user})

def accept_booking(request,id):
    obj=get_object_or_404(UserBookTableModel,booking_id=id)
    obj.status="Payment Pending"
    obj.save(update_fields=["status"])
    messages.success(request, "Accepted Booking" )
    return redirect("restro_view_table_bookings")

def reject_booking(request,id):
    obj=get_object_or_404(UserBookTableModel,booking_id=id)
    obj.status="Not Available"
    obj.save(update_fields=["status"])
    messages.error(request, "Rejected Booking" )
    return redirect("restro_view_table_bookings")


def restro_view_feedback(request):
    restaurent=request.session["restaurent_id"]
    feed=UserFeedbackModel.objects.filter(user_restaurent=restaurent)
    return render (request,'restaurants/restaurant-view-feedback.html',{'feed':feed})

def restro_view_food_orders(request):
    return render (request,'restaurants/restaurant-view-orders-food.html')

