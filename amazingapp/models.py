from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
