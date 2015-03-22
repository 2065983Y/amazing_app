__author__ = 'yanev'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazing_project.settings')

import django
django.setup()

from amazingapp.models import Maze

def populate():
<<<<<<< HEAD
	name = "Destroyer583"
	rows = 4
	cols = 4
	cells = "1000110001100011"

	add_maze(name, rows, cols, cells)

def add_maze(name, rows, cols, cells):
	maze = Maze.objects.get_or_create(name=name, rows=rows, cols=cols, cells=cells)
	return maze
	
if __name__ == '__main__':
	print "Starting population script..."
	populate()
=======
    name = "Destroyer583"
    rows = 4
    cols = 4
    cells = "1000110001100011"

    add_maze(name, rows, cols, cells)

def add_maze(name, rows, cols, cells):
    maze = Maze.objects.get_or_create(name=name, rows=rows, cols=cols, cells=cells)
    return maze

if __name__ == '__main__':
    print "Starting population script..."
    populate()
>>>>>>> 08fa5a13ca0617e56cd77aa1f713ed90c307394a
