# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from StudentLogin.models import Student_details

# Create your views here.

def home(request):
    temp = 'faculty/main.html'
    return render(request,temp,{})

class StudentList(ListView):
    template_name = 'faculty/display.html'
    model = Student_details


"""class StudentDetailView(DetailView):
    model = User
    template_name = 'StudentLogin/update.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['user_info'] = Student_details.objects.get(user=self.get_object())
        return context"""


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
