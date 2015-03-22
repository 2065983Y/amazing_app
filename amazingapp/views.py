from django.shortcuts import render, redirect
from amazingapp.algorithms.astar import aStar

from amazingapp.forms import CreateMazeForm
from amazingapp.models import Maze,UserProfile
from amazingapp.forms import UserProfileForm, UserEditForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from django.contrib.auth import  update_session_auth_hash
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.views import password_change




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
    if request.method == "POST":
        data = request.POST
        form = CreateMazeForm(data=request.POST)
        form.cells =  str(request.POST['cells'])
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
    return render(request,'about.html',{})

def my_password_change(request):
        return password_change(template_name ='password_change_form.html')

def password_change(request,
                    template_name='amazing_app/templates/registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    print password_change_form
    if post_change_redirect is None:
        post_change_redirect = reverse('password_change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': ('Password change')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request,'password_change_form.html', context)


@login_required
def password_change_done(request,
                         template_name='registration/password_change_done.html',
                         current_app=None, extra_context=None):
    context = {
        'title': ('Password change successful'),
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

@login_required
def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user

            if 'picture' in request.FILES:
                profile.avatar = request.FILES['picture']
            profile.save()
            return redirect("/")
        else:
            print profile_form.errors
    else:
        profile_form = UserProfileForm()


    return render(request, 'profile_registration.html', {'profile_form': profile_form})

@login_required
def profile_no_edit(request):
    context_dict = {}
    user = User.objects.get(username=request.user)


    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        user_profile = None

    context_dict['user'] = user
    context_dict['user_profile'] = user_profile
    return render(request, 'profile.html', context_dict)

    #if request.method == 'POST':
    #    user_profile = UserProfileForm(data=request.POST)


@login_required
def profile(request):
    context_dict = {}
    print "METHOD", request.method
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
        try:
            profile_form = UserProfileForm(instance=request.user.userprofile)
        except:
            profile_form = None
    context_dict['user_form'] = user_form
    if profile_form:
        context_dict['profile_form'] = profile_form
        context_dict['picture'] = request.user.userprofile.picture
    return render(request, "profile.html", context_dict)




