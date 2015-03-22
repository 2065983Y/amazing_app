from django.shortcuts import render
from amazingapp.models import Maze, UserProfile
# Create your views here.

def index(request):

    mules_list = UserProfile.objects.order_by('-mazes_created')[:5]
    cats_list = UserProfile.objects.order_by('-mazes_solved')[:5]

    context_dict = {'mules': mules_list, 'cats': cats_list}


    response = render(request,'index.html', context_dict)

    return response
	
def builders(request):
	return render(request,'index.html', {})

def solvers(request):
	return render(request,'index.html', {})
	
def mazes(request):
	return render(request,'index.html', {})
