from django.db import models
from django.contrib.auth.models import User

class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    solved_by = models.TextField()
    rows = models.IntegerField()
    cols = models.IntegerField()
    cells = models.TextField()
    attempts = models.IntegerField(default = 0)
#    creator = models.ForeignKey(User)
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
    email = models.CharField(max_length = 128)
    password = models.CharField(max_length=128)
    mazes_created = models.IntegerField(default=0)
    mazes_solved = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username
