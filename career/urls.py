from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('show/',views.home,name='home'),
     path('',views.home,name="home"),
         # Path to ADD Employee
    path('add_data',views.add_data,name='add_data'),
]
