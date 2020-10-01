from django.shortcuts import render
from .models import destination
# Create your views here.

def index(request):
    dest1 = destination()
    dest1.name = "Mumbai"
    dest1.desc = "the city that never sleeps"
    dest1.price = 231
    dest1.image = 'destination_1.jpg'
    return render(request,"index.html",{'dest_1': dest1})