from django.shortcuts import render
from .models import Room

def index(request):
    rooms = Room.objects.all() 
    return render(request,"hilo/index.html",context={"rooms":rooms})