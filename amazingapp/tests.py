from django.test import TestCase
from amazingapp.views import index,register
from amazingapp.models import Maze,UserProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import views



class MazeTest(TestCase):
    user = User("joe")
    u1 = User("bob")
    def create_maze(self,name = "test_maze",rows = 10,cols = 10,cells = 100,
                     solved_by =u1,attempts = 10,creator = user,solved = True):

         return Maze.objects.create(name = name,rows = rows,cols = cols,cells = cells,
                     solved_by = solved_by,attempts = attempts,creator = creator,soved = solved)

    @property
    def create_user(self):
        user = User(10)
        return UserProfile.objects.create(user = user,mazes_created = 1, mazes_solved = 1)

    def test_create_maze(self):

        m = self.create_maze()
        self.assertTrue(isinstance(m,Maze))

    def test_user_creation(self):
        u = self.create_user
        self.assertTrue(isinstance(u,UserProfile))


    def test_maze_list_view(self):
        m = self.create_maze()
        url = reverse('mazes')
        response= self.client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertIn("mazes",response.content)

    def test_create_maze_view_redirect(self):
        m = self.create_maze()
        grid = m.getOrCreateGrid()
        validity = m.is_valid(grid)
        self.assertEquals(validity,m.is_valid(grid))


    def test_index(self):
        '''
        Tests if the top 5 mules and cats are displayed
        '''

        #if site responds
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # check the mules and cats

        self.assertIn("mules",response.context)
        self.assertIn("cats",response.context)









