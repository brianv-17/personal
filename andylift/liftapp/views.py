from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = { 
        'guest' : Guest.objects.all()
    }
    return render(request, 'client.html', context)

def guest(request):
    Guest.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        comment = request.POST['comment'],
    )
    return redirect('/')