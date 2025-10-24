from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter movie name'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Enter release year'}),
        }
