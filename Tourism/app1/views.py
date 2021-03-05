from django.shortcuts import render,HttpResponse
from app1.models import Contact


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,gender=gender,desc=desc)
        contact.save()
    return render(request,"contact.html")

def forts(request):
    return render(request,"forts.html")

def beaches(request):
    return render(request,"beaches.html")

def museum(request):
    return render(request,"museum.html")

def caves(request):
    return render(request,"caves.html")

def hot_water_springs(request):
    return render(request,"hot_water_springs.html")

def temples(request):
    return render(request,"temples.html")

