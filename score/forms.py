from django import forms
from .models import Stat

class StatCreateForm(forms.ModelForm):
    class Meta:
        model = Stat
        exclude = ('player',)
        widgets = {
            'date': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'date',
                                                 'class': 'form-control'}),
            'total_score': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'total_score',
                                                 'class': 'form-control'}),
            'ob': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'ob',
                                                 'class': 'form-control'}),
            'penalty': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'penalty',
                                                 'class': 'form-control'}),
            'fw': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'fw',
                                                 'class': 'form-control'}),
            'par_on': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'par_on',
                                                 'class': 'form-control'}),
            'putt': forms.TextInput(attrs={'autocomplete': 'off',
                                                 'placeholder': 'putt',
                                                 'class': 'form-control'}),                                                                                                                                                                                         
        }
