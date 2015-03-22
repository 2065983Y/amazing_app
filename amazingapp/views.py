from django.http import HttpResponse
from django.shortcuts import render, redirect
from amazingapp.algorithms.astar import aStar
from amazingapp.models import Maze, UserProfile
from amazingapp.forms import CreateMazeForm


# Create your views here.

def index(request):
    mules_list = UserProfile.objects.order_by('-mazes_created')[:5]
    cats_list = UserProfile.objects.order_by('-mazes_solved')[:5]

    context_dict = {'mules': mules_list, 'cats': cats_list}

    response = render(request, 'index.html', context_dict)

    return response


def builders(request):
    return render(request, 'index.html', {})


def solvers(request):
    return render(request, 'index.html', {})


def mazes(request):
    return render(request, 'index.html', {})


# def index(request):
#    
#    return render(request, 'base.html', {})

#def mazes(request):
#    m = Maze.objects.get(name="Destroyer583")
#    #print m.cells
#    grid = m.getOrCreateGrid()
#
#    wayOut =  aStar(grid)
#    if(not wayOut):
#        return HttpResponse("NO WAY OUT u suck!")
#
#    return HttpResponse(m.cells)

def create_maze(request):
    if request.method == 'POST':
        form = CreateMazeForm(request.POST)
        # name = request.POST.get('name')
        # rows = request.POST.get('rows')
        # cols = request.POST.get('cols')
        # cells = request.POST.get('cells')
        if form.is_valid():
            context_dict = {'name': form.name, 'rows': form.rows, 'cols': form.cols, 'cells': form.cells}

            form.save(commit=True)

        else:
            print form.errors

    else:
        form = CreateMazeForm()
    return render(request, 'amazingapp/create_maze.html', context_dict)


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

def createMaze(request):
    return render(request, 'amazingApp/create_maze.html', {})
