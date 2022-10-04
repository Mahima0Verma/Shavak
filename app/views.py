from urllib import request
from django.shortcuts import render, HttpResponse
from re import A
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def thankyou(request):
    return render(request, 'thankyou.html')     

def contact(request):
    if request.method=='POST':   
        
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.phone = phone
        contact.message = message
        contact.save()
    
        
  
    
   
    return render(request, 'contact.html')


def sendmail(request):
    if request.method=='POST':   
        
       
       
        subject = request.POST.get('subject')
       
        message = request.POST.get('message')
        send_mail(
          
            subject,
            message,


            'mahimaverma3112@gmail.com',
            ['mahimavermakumari@gmail.com','sandeepkumarbansal0@gmail.com'],
            fail_silently=False
        )    
        messages.info(request,"Mail Send Successfully")
        return redirect('thankyou')

    else:
         messages.info(request,"Mail not Send")
         return render(request,'contact.html')




def media(request):
    return render(request, 'media.html')

def van(request):
    all_data =  Van.objects.all()
    return render(request, 'van_services.html', {'key1':all_data})

def bus(request):
    all_data = Bus.objects.all()
    return render(request, 'bus_services.html',{'key1':all_data})

def rickshaw(request):
    all_data =  Rickshaw.objects.all()
    return render(request, 'rickshaw_services.html', {'key1':all_data})
