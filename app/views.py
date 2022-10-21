from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
from app.forms import ToDoForm
from app.models import ToDo
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


class ToDosListView(ListView):
    model = ToDo
    context_object_name = 'todos'

    def get_queryset(self):
        user = self.request.user
        data = ToDo.objects.filter(user=user).order_by('-date')
        return data


@login_required(login_url='login')
def home(request):
    return redirect('todo_list')


@login_required(login_url='login')
def add_todo(request):
    if request.method == 'GET':
        form = ToDoForm()
        context = {"form": form}
        return render(request, 'add_todo.html', context)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            form = ToDoForm(data=request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect('todo_list')
            else:
                context = {"form": form}
                return render(request, 'add_todo.html', context)


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
                return redirect('todo_list')
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


@login_required(login_url='login')
def logout(request):
    logoutUser(request)
    return redirect('login')
