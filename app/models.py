from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    status_choices = {
        ('c', 'completed'),
        ('p', 'pending')
    }
    title = models.CharField(max_length=500)
    status = models.CharField(max_length=500, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority_choices = {
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)
    }
    priority = models.IntegerField(max_length=2, choices=priority_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
