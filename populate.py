__author__ = 'yanev'

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazing_project.settings')

import django

django.setup()

from amazingapp.models import Maze, UserProfile
from django.contrib.auth.models import User


def populate():
	add_maze("Destroyer583", 4, 4, "1000110001100011", 2)
	
	add_maze("Daedalus", 4, 4, "1000111111100011", 2)
	
	add_maze("John", 5, 5, "1111111111000110001100011", 2)
	
	add_maze("Jim", 5, 5, "1111100111000110001100011", 2)

	add_profile("a", "l@l.com", "1", 100, 50)
	add_profile("b", "l@l.com", "1", 14, 12)
	add_profile("c", "l@l.com", "1", 1100, 100)
	add_profile("d","l@l.com", "1", 180, 100)
	add_profile("e", "l@l.com", "1", 10, 10)
	
def add_maze(name, rows, cols, cells, attempts, solved_by = "John"):
    maze = Maze.objects.get_or_create(name=name, rows=rows, cols=cols, cells=cells, solved_by = solved_by, attempts = attempts)
    return maze

def add_profile(username, email, password, created, solved):
	user = User.objects.create_user(username= username, email=email ,password=password)
	profile = UserProfile.objects.get_or_create(user = user, email = email, password = password, mazes_created = created, mazes_solved = solved)
	return profile

if __name__ == '__main__':
    print "Starting population script..."
    populate()