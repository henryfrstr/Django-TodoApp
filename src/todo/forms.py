from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task title..'}), label='')
    due = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Due date..'}), label='')
    
    class Meta:
        model = Task
        fields = ['title', 'due']


class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task title..'}), label='')
        
    class Meta:
        model = Task
        fields = ['title', 'due', 'completed']