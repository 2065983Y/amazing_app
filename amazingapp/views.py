from django.http import HttpResponse
from django.shortcuts import render, redirect
from amazingapp.algorithms.astar import aStar
from amazingapp.models import Maze

# Create your views here.

def index(request):
    
    return render(request, 'base.html', {})

def mazes(request):
    m = Maze.objects.get(name="Destroyer583")
    #print m.cells
    grid = m.getOrCreateGrid()

    wayOut =  aStar(grid)
    if(not wayOut):
        return HttpResponse("NO WAY OUT u suck!")

    return HttpResponse(m.cells)

def pickMaze(request):
    context_dic = {}
    mazes = Maze.objects.all()
    context_dic["mazes"] = mazes
    return render(request, "amazingApp/pick_maze.html", context_dic)

def solveMaze(request, maze_name):
    context_dic = {}
    try:
        maze = Maze.objects.get(name=maze_name)
        context_dic["maze_cells"] = maze.cells
        context_dic["maze_name"] = maze.name
        context_dic["rows"] = maze.rows
        context_dic["cols"] = maze.cols
    except Maze.DoesNotExist:
        print "Maze does not exist"
        return redirect('/mazeapp/')

    return render(request, 'amazingApp/solve_maze.html', context_dic)
