from django.contrib import admin
from amazingapp.models import Maze, UserProfile


# Register your models here.

from amazingapp.models import Maze

class MazeAdmin(admin.ModelAdmin):
	list_display = ('name', 'solved_by', 'rows', 'cols', 'cells', 'attempts')
# Register your models here.

admin.site.register(Maze)
admin.site.register(UserProfile)

