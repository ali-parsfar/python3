from django.http import HttpResponse
from django.shortcuts import render
from .models import Cakes

# Create your views here.


def index(request):
    cakes = Cakes.objects.all()
    return render(request, 'index.html', {'products': cakes})


def new(request):
    return HttpResponse("New Products")
