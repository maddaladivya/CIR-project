# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cir.models import Company_details
from django.views.generic import ListView
# Create your views here.

#def Display(request):
#    objects = Company_details.objects.all()

#    for object in objects:
#        object.fields = dict((field.name, field.value_to_string(object))
                                            #for field in object._meta.field)

#    template = "StudentLogin/display.html"
#    return render(template, {'objects': objects}, request)

class CompanyList(ListView):
    template_name = 'StudentLogin/display.html'
    model = Company_details
