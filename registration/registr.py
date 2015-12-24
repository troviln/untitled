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
            return HttpResponseRedirect("/hello/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})


def login(request):

    if request.method == 'POST':
        form = EnterForm(request.POST)
        if form.is_valid():
            if form.get_user():
                auth.login(request, form.get_user())
                # �������������� �� �������� ��������� �����,
                return HttpResponseRedirect("/hello/")
    else:
        form = EnterForm()

    return render(request, 'enter_form.html', {'form': form})

def logout(request):
    auth.logout(request)
    # �������������� �� �������� ��������� ������,
    return HttpResponseRedirect("/hello/")
