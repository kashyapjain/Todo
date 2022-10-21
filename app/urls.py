from django.contrib import admin
from django.urls import path
from app.views import ToDosListView, login, signup, add_todo

urlpatterns = [
    path('', ToDosListView.as_view(), name='todo_list'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('add_todo', add_todo, name='add_todo')
]
