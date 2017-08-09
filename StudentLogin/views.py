# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cir.models import Company_details
from django.views.generic import ListView
# Create your views here.

def home(request):
    temp = 'StudentLogin/home.html'
    return render(request,temp,{})
    

class CompanyList(ListView):
    template_name = 'StudentLogin/display.html'
    model = Company_details
