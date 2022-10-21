from django.contrib import admin
from django.urls import path
from app.views import ToDosListView, login, signup, add_todo, logout, home, delete_todo, change_status

urlpatterns = [
    path('', home, name='home'),
    path('todo_list', ToDosListView.as_view(), name='todo_list'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('add_todo', add_todo, name='add_todo'),
    path('logout', logout, name='logout'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    path('change_status/<int:todo_id>/<str:status>', change_status),
]
