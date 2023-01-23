from django.shortcuts import render
from django.http import HttpResponse
from .models import department, architect, booking
from . forms import bookingform
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,"about.html")

def departments(request):
    dict_dept={
        'dept': department.objects.all()
    }
    return render(request,"department.html", dict_dept)

def architects(request):
    dict_arch={
        'arch': architect.objects.all()
    }
    return render(request,"architects.html", dict_arch)

def bookings(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = bookingform()
    dict_form = {
        'form': form
    }
    return render(request,"booking.html", dict_form)

def contact(request):
    return render(request,"contact.html")