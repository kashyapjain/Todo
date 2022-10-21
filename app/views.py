from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    form = UserCreationForm()

    context = {'form': form}

    return render(request, 'signup.html', context)
