__author__ = 'trigger'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from registration.enter_form import EnterForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):

    if request.method == 'POST':
        form = EnterForm(request.POST)
        if form.is_valid():
            if form.get_user():
                auth.login(request, form.get_user())
                # �������������� �� �������� ��������� �����,
                return HttpResponseRedirect("/blog/")
    else:
        form = EnterForm()

    return render(request, 'registration/enter_form.html', {'form': form})

def logout(request):
    auth.logout(request)
    # �������������� �� �������� ��������� ������,
    return HttpResponseRedirect("/blog/")
