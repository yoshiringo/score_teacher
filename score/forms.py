from django import forms
from .models import Stat

class StatCreateForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ('date', 'total_score', 'ob', 'penalty', 'fw', 'par_on', 'putt')
        labels = {
            'date':'日付',
            'total_score':'スコア',
            'ob':'OB',
            'penalty':'ペナルティ数',
            'fw':'FWキープ率',
            'par_on':'パーオン率',
            'putt':'パット数',
        }