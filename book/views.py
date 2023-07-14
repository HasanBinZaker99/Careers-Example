from django.shortcuts import render
from book.models import tata
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Function to render Homepage
def home(request):
    list = tata.objects.all().order_by('-id')
    return render(request,"home.html",{"lists":list})

# Function to ADD Employee
def add_data(request):
    if request.method == "POST":
        if request.POST.get('date_time') \
            and request.POST.get('trade_code') \
            and request.POST.get('high') \
            and request.POST.get('low') \
            and request.POST.get('open') \
            and request.POST.get('close')\
            and request.POST.get('volume'):
            data = tata()
            data.date_time = request.POST.get('date_time')
            data.trade_code = request.POST.get('trade_code')
            data.high = request.POST.get('high')
            data.low = request.POST.get('low')
            data.open = request.POST.get('open')
            data.close = request.POST.get('close')
            data.volume = request.POST.get('volume')
            data.save()
            messages.success(request,"Data added successfully !")
            return HttpResponseRedirect("/")
        else:
            return render(request,'add.html')
