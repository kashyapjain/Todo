from django.forms import ModelForm
from app.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'status', 'priority']
