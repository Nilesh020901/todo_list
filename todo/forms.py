from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        models=Todo
        field="__all__"
        