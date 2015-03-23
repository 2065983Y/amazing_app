from django.db import models
from django.contrib.auth.models import User



class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rows = models.IntegerField()
    cols = models.IntegerField()
    cells = models.TextField()
    solved_by = models.TextField()
    attempts = models.IntegerField(default = 0)
#    creator = models.ForeignKey(User)
    __grid = None


    def getOrCreateGrid(self):
        if(self.__grid):
            return self.__grid

        self.cells = [str(x) for x in self.cells if x == "1" or x == "0"] # remove peski unicode
        print self.rows, self.cols
        grid = []
        index = 0
        for i in xrange(self.rows):
            row = []
            for j in xrange(self.cols):
                row += self.cells[index]
                index += 1
            grid += [row]
        print "WORK", grid
        self.__grid = grid
        return grid


    def __unicode__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    mazes_created = models.IntegerField(default=0)
    mazes_solved=models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

