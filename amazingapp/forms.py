from django import forms
from django.contrib.auth.models import User
from amazingapp.models import Maze, UserProfile
class CreateMazeForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Name of your maze", required=True)
    rows = forms.ChoiceField(choices=[(int(x),x) for x in range(3, 21)], help_text="Rows", required=True)
    cols = forms.ChoiceField(choices=[(int(x),x) for x in range(3, 21)], help_text="Columns", required=True)
    cells = forms.CharField(widget=forms.MultipleHiddenInput())

    class Meta:
        model = Maze
        fields = ['name', 'rows', 'cols', 'cells']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email', 'password')


class UserProfileForm(forms.ModelForm):
    picture=forms.ImageField(help_text="Choose a profile image ", required=False)
    class Meta:
        model = UserProfile
        fields = ('picture',)

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email')

