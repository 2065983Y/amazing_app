from django import forms
from amazingapp.models import Maze


class CreateMazeForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Name of your maze", required=True)
    rows = forms. ChoiceField(choices=[x for x in range(3, 20)], help_text="rows", required=True)
    cols = forms.ChoiceField(choices=[x for x in range(3, 20)], help_text="columns", required=True)

    class Meta:
        model = Maze
        fields = ('name', 'rows', 'cols', 'cells')



