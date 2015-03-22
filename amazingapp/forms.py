from django import forms
from amazingapp.models import Maze


class CreateMazeForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Name of your maze", required=True)
    rows = forms.IntegerField(help_text="Rows", required=True)
    cols = forms.IntegerField (help_text="Columns", required=True)
    cells = forms.CharField(widget=forms.MultipleHiddenInput())

    class Meta:
        model = Maze
        fields = ['name', 'rows', 'cols', 'cells']





