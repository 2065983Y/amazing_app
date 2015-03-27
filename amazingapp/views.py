from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from amazingapp.algorithms.astar import aStar

from amazingapp.forms import CreateMazeForm
from amazingapp.models import Maze
from django.shortcuts import redirect
from models import UserProfile
from amazingapp.forms import UserForm, UserProfileForm,UserEditForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    total_mazes = 0
    unsolved = {}
    users = UserProfile.objects.all()
    mules_list = UserProfile.objects.order_by('-mazes_created')[:5]
    cats_list = UserProfile.objects.order_by('-mazes_solved')[:5]
    context_dict = {'mules': mules_list, 'cats': cats_list}
    context_dict['unsolved_mazes'] = Maze.objects.all().filter(solved=False).count()
    context_dict['mazes_num'] = Maze.objects.all().count()
    response = render(request, 'amazingApp/index.html', context_dict)
    return response


def builders(request):
    return render(request, 'amazingApp/builders.html', {'users': UserProfile.objects.all()})


def created(request):
    return render(request,'amazingApp/maze_created.html', {})


def solvers(request):
    return render(request, 'amazingApp/solvers.html', {'users': UserProfile.objects.all()})


def mazes(request):
    return render(request, 'amazingApp/view_mazes.html', {'mazes': Maze.objects.all()})


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

@login_required
def create_maze(request):
    context_dict = {}
    if request.method == "POST":
        form = CreateMazeForm(data=request.POST)
        #try:
        maze = form.save(commit=False)
    #form.cells =  str(request.POST['cells'])
    #print form
    #print request.POST
    #print data["Rows"], data["Columns"], data["name"]
    #form.rows = int(data["Rows"])
    #form.cols = int(data["Columns"])
    #form.name = data["name"]
    ##form.save(commit=False)
    #print type(form.rows), type(form.cols)

        grid = maze.getOrCreateGrid()
        if not grid:
            return redirect("/mazeapp/create/")
        if grid:
    #        print form.is_valid(grid)
            if form.is_valid(grid):
                maze.creator = request.user
                builder = UserProfile.objects.get(user=request.user)
                builder.mazes_created += 1
                builder.save()
                #maze.solved = False
                form.save(commit=True)
                return redirect("/mazeapp/created")
            else:
                if not form.systemPath:
                    form._errors["unsolvable"] = [u'Maze does not have a path, custom start & end coming soon']
                    context_dict["unsolvable"] = 'Maze does not have a path, custom start & end coming soon'
            # print form.errors
        else:
            context_dict["unsolvable"] = "Please do not submit an empty maze"
        #except:
        #    pass
    else:
        form = CreateMazeForm()
    context_dict["form"] = form
    return render(request, "amazingApp/create_maze.html", context_dict)


def pickMaze(request):
    context_dic = {}
    mazes = Maze.objects.all()
    context_dic["mazes"] = mazes
    return render(request, "amazingApp/pick_maze.html", context_dic)


def solveMaze(request, maze_name):
    context_dic = {}
    maze = Maze.objects.get(name=maze_name)
    context_dic["maze_name"] = maze.name
    if request.method == "POST":
        #print "USER", request.user, "solved by:", maze.solved_by
        #print "somtthing", request.user in maze.solved_by

        if not request.user.is_authenticated():
            #maybe give something more to the poor anonymous(guest) user here but that's all for now
            return redirect('/mazeapp/') # perhaps give the guest user another screen to improve their testing experice of the site
        solver = UserProfile.objects.get(user=request.user)
        if not maze.solved_by.all():
            maze.solved_by.add(request.user)
            solver.mazes_solved += 1
            solver.save()
        elif request.user not in Maze.objects.get(name=maze_name).solved_by.all():
            maze.solved_by.add(request.user)
            solver.mazes_solved += 1
            solver.save()
        maze.solved = True
        maze.save()
    else:
        try:
            maze.attempts += 1
            context_dic["maze_cells"] = maze.cells
            context_dic["maze_rows"] = maze.rows
            context_dic["maze_cols"] = maze.cols
            maze.save()
        except Maze.DoesNotExist:
            print "Maze does not exist"
            return redirect('/mazeapp/')

    context_dic['maze_solved'] = maze.solved
    context_dic['maze_attempts'] = maze.attempts - 1

    return render(request, 'amazingApp/solve_maze.html', context_dic)


def about(request):
    return render(request, 'amazingApp/about.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'amazingApp/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/mazeapp/')


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/mazeapp/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Oopps.It seems that your account has been disabled")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Wrong username or password.")
    else:
        return render(request, 'amazingApp/login.html', {})


def register_profile(request):

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.email = "a@a.com"
            profile.user = request.user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return redirect("/mazeapp/")
        else:
            print profile_form.errors
    else:
        profile_form = UserProfileForm()
    return render(request, "amazingApp/profile_registration.html", {'profile_form': profile_form})


@login_required
def edit_profile(request):
    context_dict = {}
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile)

        if profile_form.is_valid and user_form.is_valid:
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            user.save()
            profile.save()
        else:
            print user_form.errors
            print profile_form.errors
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['picture'] = request.user.userprofile.picture
    return render(request, "amazingApp/profile.html", context_dict)
