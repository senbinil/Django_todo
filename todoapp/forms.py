from todoapp.models import Task
from django import forms
from django.forms import widgets
from django.forms.fields import CharField, IntegerField


class Myform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Task details'}),
            'priority':forms.NumberInput(attrs={'class':'form-control text-center','placeholder':'Task Priority'}),
            'date':forms.DateInput(attrs={'class':'form-control text-center','type':'date'})
        }
