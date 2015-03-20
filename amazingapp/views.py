from django.http import HttpResponse
from django.shortcuts import render
from amazingapp.models import Maze

# Create your views here.

def index(request):
    
    return render(request, 'base.html', {})

def mazes(request):
    return HttpResponse(Maze.objects.get(name="Destroyer583").cells)
