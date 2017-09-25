# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from StudentLogin.models import Student_details
from django.core.management.base import BaseCommand
from django.utils import timezone
from faculty.models import Announcements

# Create your views here.

def home(request):
    temp = 'faculty/main.html'
    return render(request,temp,{})

class StudentList(ListView):
    template_name = 'faculty/display.html'
    model = Student_details

def Announcement(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        date = request.POST.get('date')
        u = Announcements.objects.create(link=link, expiry_date=date)
        u.save()
        return render(request,'faculty/main.html',{})
    return render(request,'faculty/link.html',{})

class Command(BaseCommand):
    help = 'Deletes expired rows'

    def handle(self, *args, **options):
        now = timezone.now()
        Announcements.objects.filter(expire_time__lt=now).delete()


def upload(request, pk):
    a = Student_details.objects.get(id=pk)
    if request.method == 'POST':
        u = Student_details.objects.get(id=pk)
        u.s1 = request.POST.get('s1')
        u.s2 = request.POST.get('s2')
        u.s3 = request.POST.get('s3')
        u.s4 = request.POST.get('s4')
        u.s5 = request.POST.get('s5')
        u.s6 = request.POST.get('s6')
        u.CGPA = request.POST.get('CGPA')
        u.no_of_current_Arrears = request.POST.get('carrears')
        u.no_of_history_Arrears = request.POST.get('harrears')
        u.PlacementStatus = request.POST.get('placementstatus')
        u.PlacementStatusFinal = request.POST.get('placementstatusfinal')
        u.save()
        return HttpResponseRedirect('/faculty/home')
    return render(request,'faculty/upload.html',{'a':a})
