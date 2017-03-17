# coding=utf-8

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import auth

# Create your views here.
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Student.form import RegisterForm
from Student.models import StudentInfo


def open_register_page(request):
    args = {}
    args['form'] = UserCreationForm()
    args['myform'] = RegisterForm()
    args['nextform'] = StudentInfo()
    return render(request, 'register.html', args)


def open_signin_page(request):
    form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})


def useradd(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = UserCreationForm(request.POST)
        myform = RegisterForm(request.POST)
        # nextform = StudentInfo(request.POST)
        args['form'] = form
        args['myform'] = myform
        username = request.POST['username']
        password = request.POST['password1']
        if form.is_valid():
            form.save()
            name = request.POST['name']
            surname = request.POST['surname']
            lat = request.POST['lat']
            lat = lat.replace('(', '')
            lat = lat.replace(')', '')
            lat=lat.split(',')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            student = StudentInfo(user=user, name=name, surname=surname, lat=lat[0], lng=lat[1])
            student.save()
            return redirect('http://127.0.0.1:8000/index')
        else:
            return render_to_response("register.html", args)

def logins(request):
    args = {}
    args.update(csrf(request))
    args['form'] = AuthenticationForm(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('http://127.0.0.1:8000/index')
    else:
        args['login_error'] = 'Пользователь не найден'
        return render_to_response("signin.html", args)
    return redirect(request.META['HTTP_REFERER'])


def logout(request):
    auth.logout(request)
    return redirect('/')
