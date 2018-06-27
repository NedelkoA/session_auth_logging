from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from .forms import LoginForm
from .models import Task
from django.contrib.auth.decorators import login_required


class TaskView(ListView):
    model = Task
    template_name = 'test_auth/login_form.html'


def index(request):
    return render(request, 'test_auth/login_form.html', {'form': LoginForm()})


@login_required
def success_page(request):
    return render(request, 'test_auth/success.html', {})


def my_auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/success')
            return render(request, 'test_auth/login_form.html', {
                'form': LoginForm(),
                'error': 'text'
            })

