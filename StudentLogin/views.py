# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from StudentLogin.forms import UserForm
from cir.models import Company_details
from django.views.generic import ListView
# Create your views here.

def home(request):
    temp = 'StudentLogin/home.html'
    return render(request,temp,{})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        if registered == True:
            return HttpResponseRedirect('/student/display')
        else:
            return HttpResponse("Username already in use.")
    else:
        user_form = UserForm()
    return render(request,
            'StudentLogin/register.html',
            {'user_form': user_form,'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/student/display')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request,'StudentLogin/login.html', {})
class CompanyList(ListView):
    template_name = 'StudentLogin/display.html'
    model = Company_details
