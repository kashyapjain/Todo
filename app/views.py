from xml.dom import UserDataHandler
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from app.forms import ToDoForm
from app.models import ToDo
from django.views.generic import ListView


class ToDosListView(ListView):
    model = ToDo


def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm()
        context = {"form": form, "todos": ToDosListView.as_view()}
        return render(request, 'home.html', context)


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            context = {"form": form}
            return render(request, 'home.html', context)


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {"form": form}
            return render(request, 'login.html', context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        print(form.as_table())
        context = {'form': form}
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context)
