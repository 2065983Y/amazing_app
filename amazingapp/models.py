from django.db import models
from django.contrib.auth.models import User

# Create your models here.
<<<<<<< HEAD
class Maze(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	creator = models.CharField(max_length = 128)
	solved_by = models.CharField(max_length = 128)
	attempts = models.IntegerField(default = 0)
	dimensions = models.IntegerField(default = 0)
	difficulty = models.IntegerField(default = 0)
	rating = models.FloatField(default = 0.0)
	cols = models.IntegerField()
	cells = models.TextField()
	
	def __unicode__(self):
		return self.name
		
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	email = models.CharField(max_length = 128)
	password = models.CharField(max_length = 128)
	achievements = models.IntegerField(default = 0)
	mazes_created = models.IntegerField(default = 0)
	mazes_solved = models.IntegerField(default = 0)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username
=======


class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rows = models.IntegerField()
    cols = models.IntegerField()
    cells = models.TextField()
    creator = models.ForeignKey(User)
    __grid = None

    def __unicode__(self):
        return self.name

    def getOrCreateGrid(self):
        if(self.__grid):
            return self.__grid
        grid = []
        index = 0
        for i in xrange(self.rows):
            row = []
            for j in xrange(self.cols):
                row += self.cells[index]
                index += 1
            grid += [row]
        self.__grid = grid
        return grid


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)

>>>>>>> 08fa5a13ca0617e56cd77aa1f713ed90c307394a
