from django import forms
from django.forms import fields
from .models import Text

class TaskForm (forms.ModelForm):
    addtext = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Task', 'class':'form-control'}))
    complete = forms.CheckboxInput()
    class Meta:
        model = Text
        fields = '__all__'