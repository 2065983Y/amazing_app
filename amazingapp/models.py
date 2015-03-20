from django.db import models

# Create your models here.

class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rows = models.IntegerField()
    cols = models.IntegerField()
    cells = models.TextField()

    def __unicode__(self):
        return self.name