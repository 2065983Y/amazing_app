from django.test import TestCase
from amazingapp.views import index,register
from amazingapp.models import Maze,UserProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import views

# Helper method, for creating mazes
def add_maze(name, rows, cols, cells, attempts, solved, creator):
		maze = Maze.objects.get_or_create(name=name, rows=rows, cols=cols, cells=cells,
                                      attempts=attempts, solved = solved, creator = creator)[0]
		return maze	 

class ModelTests(TestCase):
	#Creating users
	def setUp(self):
		u = User.objects.create(username='test')
		u.set_password('test')
		u.save()
		solver = User.objects.create(username='solver')
		solver.set_password('solver')
		solver.save()
	
	# Test for adding user
	def test_add_user(self):
		u = User.objects.get(username = 'test')
		p = UserProfile.objects.create(user=u, mazes_created=1, mazes_solved=1)
		p.save()
		self.assertEqual(u.username=='test', True)
	
	# Test for tracking the creator of mazes
	def test_add_maze_creator(self):
		u = User.objects.get(username='test')
		solver = User.objects.get(username='solver')
		m = Maze.objects.create(name="test1", rows=3, cols=3, cells=9,
                                      attempts=0, solved = True, creator = u)
		m.solved_by.add(solver)
		m.save()
		self.assertEqual(m.creator==u, True)

class ViewTest(TestCase):
	
	# Test for display of table of mazes
	def test_maze_list_view(self):
		u = User.objects.create(username='test')
		u.set_password('test')
		u.save()
		de = add_maze("Destroyer583", 4, 4, "1000110001100011", 2,  True, u)
		de.solved_by.add(u)
		de.save()
		response = self.client.get(reverse('mazes'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Destroyer583")
		num_mazes = len(response.context['mazes'])
		self.assertEqual(num_mazes , 1)
	
	# Test for display of table of builders
	def test_maze_list_builders(self):
		user = User.objects.create(username='user')
		user.set_password('user')
		user.save()
		p = UserProfile.objects.create(user=user, mazes_created=1, mazes_solved=1)
		p.save()
		de = add_maze("Labirintas", 4, 4, "1000110001100011", 2,  True, user)
		de.solved_by.add(user)
		de.save()
		response = self.client.get(reverse('builders'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "user")
		
	# Test for display of table of solvers
	def test_maze_list_solvers(self):
		user = User.objects.create(username='user')
		user.set_password('user')
		user.save()
		p = UserProfile.objects.create(user=user, mazes_created=1, mazes_solved=1)
		p.save()
		de = add_maze("Labirintas", 4, 4, "1000110001100011", 2,  True, user)
		de.solved_by.add(user)
		de.save()
		response = self.client.get(reverse('solvers'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "user")
		
	# Test for display of top five mules/cats
	def test_index(self):
		user = User.objects.create(username='user')
		user.set_password('user')
		user.save()
		p = UserProfile.objects.create(user=user, mazes_created=2, mazes_solved=2)
		p.save()
		user1 = User.objects.create(username='user1')
		user1.set_password('user1')
		user1.save()
		p1 = UserProfile.objects.create(user=user1, mazes_created=2, mazes_solved=2)
		p1.save()
		user2 = User.objects.create(username='user2')
		user2.set_password('user2')
		user2.save()
		p2 = UserProfile.objects.create(user=user2, mazes_created=3, mazes_solved=3)
		p2.save()
		user3 = User.objects.create(username='user3')
		user3.set_password('user3')
		user3.save()
		p3 = UserProfile.objects.create(user=user3, mazes_created=4, mazes_solved=4)
		p3.save()
		user4 = User.objects.create(username='user4')
		user4.set_password('user4')
		user4.save()
		p4 = UserProfile.objects.create(user=user4, mazes_created=5, mazes_solved=5)
		p4.save()
		response = self.client.get(reverse('index'))
		user5 = User.objects.create(username='lazy_guy')
		user5.set_password('lazy_guy')
		user5.save()
		p5 = UserProfile.objects.create(user=user5, mazes_created=1, mazes_solved=1)
		p5.save()
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "user2")
		self.assertContains(response, "user3")
		self.assertContains(response, "user4")
		self.assertContains(response, "user1")
		self.assertContains(response, "user")
		self.assertNotContains(response, "lazy_guy")
	
