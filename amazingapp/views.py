from django.shortcuts import render, redirect
from amazingapp.algorithms.astar import aStar

from amazingapp.forms import CreateMazeForm
from amazingapp.models import Maze
from django.shortcuts import redirect




# Create your views here.

def index(request):
    total_mazes = 0
    unsolved = {}
    #all_userprofiles = UserProfile.objects.all()
    #mules_list = UserProfile.objects.order_by('-mazes_created')[:5]
    #cats_list = UserProfile.objects.order_by('-mazes_solved')[:5]
    #for profile in all_userprofiles:
    #    print profile
    #    total_mazes += profile.mazes_created
    #for profile in all_userprofiles:
    #    unsolved[profile] = total_mazes - profile.mazes_solved
    #context_dict = {'mules': mules_list, 'cats': cats_list, 'unsolved': unsolved}
    response = render(request, 'amazingApp/index.html', {})
    return response


def builders(request):
    return render(request, 'amazingApp/index.html', {})

def solvers(request):
    return render(request, 'amazingApp/index.html', {})


def mazes(request):
    return render(request, 'amazingApp/index.html', {})


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
    if request.method == "POST":
        data = request.POST
        form = CreateMazeForm(data=request.POST)
        #form.cells =  str(request.POST['cells'])
        #print form
        #print request.POST
        #print data["Rows"], data["Columns"], data["name"]
        #form.rows = int(data["Rows"])
        #form.cols = int(data["Columns"])
        #form.name = data["name"]
        ##form.save(commit=False)
        #print type(form.rows), type(form.cols)

        print "valid", form.is_valid()
        if form.is_valid():
            form.save()
        else:
            print form.errors

    else:
        form = CreateMazeForm()
    return render(request, "amazingApp/create_maze.html", {"form": form})


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
        context_dic["maze_rows"] = maze.rows
        context_dic["maze_cols"] = maze.cols
    except Maze.DoesNotExist:
        print "Maze does not exist"
        return redirect('/mazeapp/')

    return render(request, 'amazingApp/solve_maze.html', context_dic)


def createMaze(request):
    return render(request, 'amazingApp/create_maze.html', {})


def about(request):
    return render(request, 'about.html', {})



