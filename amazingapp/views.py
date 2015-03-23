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
            profile.user = request.user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            return redirect("/mazeapp")
        else:
            print profile_form.errors
    else:
        profile_form = UserProfileForm()
    return render(request, "amazingApp/profile_registration.html", {'profile_form': profile_form})

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

