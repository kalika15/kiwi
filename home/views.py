import email
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    #return HttpResponse("This is a homepage")
    context={
        "variable":"This is a set"
        }
    return render(request,'index.html',context)

def services(request):
    #return HttpResponse("This is a servicepage")
    return render(request,'services.html')
def menwear(request):
    return render(request,'menwear.html')
def kidswear(request):
    return render(request,'kidswear.html')


def contact(request):
   # return HttpResponse("This is a contactpage")
   if request.method=="POST":
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       inputAddress=request.POST.get('inputAddress')
       Landmark=request.POST.get('Landmark')
       inputCity=request.POST.get('inputCity')
       inputZip=request.POST.get('inputZip')
       desc=request.POST.get('desc')
       contact=Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, inputAddress=inputAddress, Landmark=Landmark, inputCity=inputCity,inputZip=inputZip,desc=desc, date=datetime.today())
       contact.save()
       messages.success(request, 'Your message has been sent!')

   return render(request,'contact.html')
    