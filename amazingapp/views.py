from django.http import HttpResponse
from django.shortcuts import render
from amazingapp.algorithms.astar import aStar
from amazingapp.models import Maze

# Create your views here.

def index(request):
    
    return render(request, 'base.html', {})

def mazes(request):
    m = Maze.objects.get(name="Destroyer583")
    #print m.cells
    grid = m.getOrCreateGrid()

    wayOut, moves =  aStar(grid)
    if(not wayOut):
        return HttpResponse("NO WAY OUT u suck!")

    return HttpResponse(m.cells)
