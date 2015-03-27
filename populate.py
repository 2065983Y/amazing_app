__author__ = 'yanev'

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazing_project.settings')

import django

django.setup()

from amazingapp.models import Maze, UserProfile
from django.contrib.auth.models import User

def add_user(username, email, password):
	try:
		u = User.objects.get(username=username)
	except:
		u = User.objects.create_user(username, email, password)
	return u

def add_user_profile(user, mazes_created, mazes_solved):
	p = UserProfile.objects.get_or_create(user=user, mazes_created=mazes_created, mazes_solved=mazes_solved)[0]
	return p

def add_maze(name, rows, cols, cells, attempts, solved, creator):
	maze = Maze.objects.get_or_create(name=name, rows=rows, cols=cols, cells=cells,
                                      attempts=attempts, solved = solved, creator = creator)[0]
	return maze
	
def populate():

	# Users
	fox = add_user('fox', 'fox@student.gla.ac.uk', 'fox')
	fox.save()
	dog = add_user('dog', 'dog@student.gla.ac.uk', 'dog')
	dog.save()
	test = add_user('test', 'test@student.gla.ac.uk', 'test')
	test.save()
	
	# User profiles
	Fox = add_user_profile(fox, 5, 2)
	Fox.save()
	Dog = add_user_profile(dog, 3, 4)
	Dog.save()
	Test = add_user_profile(test, 4, 3)
	Test.save()
	
	test1 = add_maze("Test1", 4, 4, "1000110001100011", 1,  True, fox)
	test1.solved_by.add(dog)
	test1.save()
	test2 = add_maze("Test2", 4, 4, "1000010001100011", 2,  True, fox)
	test2.solved_by.add(dog)
	test2.save()
	test3 = add_maze("Test3", 4, 4, "1000110001100011", 3,  True, fox)
	test3.solved_by.add(dog)
	test3.save()
	test4 = add_maze("Test4", 4, 4, "1000110001100011", 2,  False, dog)
	test4.save()
	test5 = add_maze("Test5", 4, 4, "1000110001100011", 2,  True, dog)
	test5.solved_by.add(test)
	test5.save()
	test6 = add_maze("Test6", 4, 4, "1000110001100011", 1,  True, test)
	test6.solved_by.add(dog)
	test6.save()
	test7 = add_maze("Test7", 4, 4, "1000110001100011", 2,  False, test)
	test7.save()
	test8 = add_maze("Test8", 4, 4, "1000110001100011", 2,  False, test)
	test8.save()
	de = add_maze("Destroyer583", 4, 4, "1000110001100011", 2,  True, fox)
	de.solved_by.add(test)
	de.save()
	labas = add_maze("Labas", 4, 4, "1000110001101011", 5,  True, dog)
	labas.solved_by.add(fox)
	labas.save()
	lab = add_maze("Lab", 4, 4, "101011001100011", 1,  True, fox)
	lab.solved_by.add(test)
	lab.save()
	circus = add_maze("Circus", 4, 4, "1111100111000110001100011", 2,  True, test)
	circus.solved_by.add(fox)
	circus.save()


	
if __name__ == '__main__':
    print "Starting population script..."
    populate()