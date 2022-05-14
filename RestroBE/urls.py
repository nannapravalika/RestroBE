"""RestroBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from mainapp import views as main_views
from adminapp import views as admin_views
from restaurentapp import views as restro_views
from userapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #main
    path ('',main_views.index,name="index"),
    path ('about',main_views.about,name="about"),
    path ('contact',main_views.contact,name="contact"),
    path ('service',main_views.service,name="service"),
    
    #admin
    path('admin-login',admin_views.admin_login,name="admin_login"),
    path('admin-dashboard',admin_views.admin_dashboard,name="admin_dashboard"),
    path('admin-feedback',admin_views.admin_feedback,name="admin_feedback"),
    path('admin-view-bookings',admin_views.admin_view_bookings,name="admin_view_bookings"),
    path('admin-view-customers',admin_views.admin_view_customers,name="admin_view_customers"),
    path('admin-view-orders',admin_views.admin_view_orders,name="admin_view_orders"),
    path('admin-view-requests',admin_views.admin_view_requests,name="admin_view_requests"),
    path("accept_restaurent/<int:id>/",admin_views.accept_restaurant,name="accept-restaurent"),
    path("reject_restaurent/<int:id>/",admin_views.reject_restaurant,name="reject-restaurent"),
    path('admin-view-restaurent-menu',admin_views.admin_view_restaurant_menu,name="admin_view_restaurant_menu"),
    path('admin-view-restaurents',admin_views.admin_view_restaurants,name="admin_view_restaurants"),
    
    
    
    #restaurant
    path ('restro-login',restro_views.restro_login,name="restro_login"),
    path ('restro-reg',restro_views.restro_reg,name="restro_reg"),
    path ('restro-dashboard',restro_views.restro_dashboard,name="restro_dashboard"),
    path ('restro-add-menu',restro_views.restro_add_menu,name="restro_add_menu"),
    path ('restro-view-menu',restro_views.restro_view_menu,name="restro_view_menu"),
    path ('restro-edit-menu',restro_views.restro_edit_menu,name="restro_edit_menu"),
    path ('restro-view-feedback',restro_views.restro_view_feedback,name="restro_view_feedback"),
    path ('restro-food-orders',restro_views.restro_view_food_orders,name="restro_view_food_orders"),
    path ('restro-table_bookings',restro_views.restro_view_table_bookings,name="restro_view_table_bookings"),
    
    #customer
    path ('user-login',user_views.user_login,name="user_login"),
    path ('user-reg',user_views.user_reg,name="user_reg"),
    path ('user-dashboard',user_views.user_dashboard,name="user_dashboard"),
    path ('user-profile',user_views.user_profile,name="user_profile"),
    path ('user-book-table',user_views.user_book_table,name="user_book_table"),
    path ('user-view-bookings',user_views.user_view_bookings,name="user_view_bookings"),
    path ('user_book_table_res/<int:id>/',user_views.user_book_table_res,name="user_book_table_res"),
    path ('user-view-orders',user_views.user_view_orders,name="user_view_orders"),
    path ('user-feedback',user_views.user_feedback,name="user_feedback"),
    path ('user-view-menu',user_views.user_view_menu,name="user_view_menu"),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)