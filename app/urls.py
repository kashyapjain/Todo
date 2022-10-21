from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('addtodo', add_todo, name='addtodo')
]
