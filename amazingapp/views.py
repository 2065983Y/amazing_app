from django.http import HttpResponse
from django.shortcuts import render
from amazingapp.algorithms.astar import aStar
from amazingapp.models import Maze
from amazingapp.forms import CreateMazeForm


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

@login_required
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
        form=CreateMazeForm()
    return render(request, 'amazingapp/create_maze.html', context_dict)





