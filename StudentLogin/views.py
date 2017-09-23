# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from StudentLogin.forms import UserForm
from StudentLogin.models import Student_details
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
            user = user_form.save(commit=False)
            user.user = request.user
            user.set_password(user.password)
            user.save()
            registered = True
        if registered == True:
            return HttpResponseRedirect('/student/profile/%d/'%user.id)
        else:
            return HttpResponse("Username already in use.")
    else:
        user_form = UserForm()
    return render(request,
            'StudentLogin/register.html',
            {'user_form': user_form,'registered': registered})
def profile(request,ak):
    if request.method == 'POST':
        user = User.objects.get(id=ak)
        name = request.POST.get('name')
        middlename = request.POST.get('middleName')
        lastname = request.POST.get('lastName')
        eligibility = request.POST.get('eligibility')
        course = request.POST.get('course')
        branchbt = request.POST.get('branchbt')
        branchmt = request.POST.get('branchmt')
        print branchbt
        print branchmt
        if branchbt == " ":
            branch = branchmt
        elif branchmt == " ":
            branch = branchbt
        else:
            branch = " "
        rollno = request.POST.get('rollno')
        massoffer = request.POST.get('massOffer')
        campus = request.POST.get('campus')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('DOB')
        tenthper = request.POST.get('tenth_percentage')
        twelthper = request.POST.get('twelth_percentage')
        stay = request.POST.get('stay')
        Interndetails = request.POST.get('Internship_details')
        jobInterest = request.POST.get('job_Interest')
        tenthboard = request.POST.get('tenth_board')
        tenthyearofpass = request.POST.get('tenth_year_of_passing')
        twelthboard = request.POST.get('twelth_board')
        twelthyearofpass = request.POST.get('twelth_year_of_passing')
        gapreason= request.POST.get('gap_in_studies_with_reason')
        address = request.POST.get('address')
        district = request.POST.get('district')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        UGmarks = request.POST.get('UG_marks')
        UGaggr= request.POST.get('UG_aggr')
        coursePG = request.POST.get('course_PG')
        UGspe= request.POST.get('UG_specialiazation')
        UGcollege = request.POST.get('UG_college')
        UGyearpass = request.POST.get('UG_year_of_passing')
        gatescore= request.POST.get('gate_score')
        ApptoPG= request.POST.get('Applicable_to_PG')
        obprofile = request.POST.get('ob_profile')
        expr = request.POST.get('expr')
        u = Student_details.objects.create(user=user,name=name, middleName=middlename, lastName=lastname, eligibility=eligibility,
                                           course=course, branch=branch, rollno=rollno, massOffer= massoffer,
                                           campus=campus, gender=gender, DOB=dateofbirth, tenth_percentage=tenthper,
                                           twelth_percentage=twelthper,stay=stay, Internship_details=Interndetails,
                                           job_Interest= jobInterest, tenth_board= tenthboard,tenth_year_of_passing=tenthyearofpass,
                                           twelth_board= twelthboard, twelth_year_of_passing=twelthyearofpass,
                                           gap_in_studies_with_reason=gapreason, permanent_address=address, district=district,
                                           state=state,country=country,pin=pin,contact=contact,UG_marks=UGmarks,
                                           UG_aggr=UGaggr,course_PG=coursePG,UG_specialiazation=UGspe,UG_college=UGcollege,
                                           UG_year_of_passing=UGyearpass,gate_score=gatescore,Applicable_to_PG=ApptoPG,
                                           ob_profile=obprofile,expr=expr)
        u.save()
        return HttpResponseRedirect('/student/login')
    return render(request,
            'StudentLogin/profile.html',
            {})


class CompanyList(ListView):
    template_name = 'StudentLogin/display.html'
    model = Company_details


def index(request):
    temp = 'StudentLogin/index.html'
    return render(request,temp,{})

def edit(request,ak):
    if request.method == 'POST':
        u = User.objects.get(id=ak)
        u.name = request.POST.get('name')
        u.middleName = request.POST.get('middleName')
        u.lastName = request.POST.get('lastName')
        u.massOffer = request.POST.get('massOffer')
        u.DOB = request.POST.get('DOB')
        u.tenth_percentage = request.POST.get('tenth_percentage')
        u.twelth_percentage = request.POST.get('twelth_percentage')
        u.Internship_details = request.POST.get('Internship_details')
        u.tenth_board = request.POST.get('tenth_board')
        u.twelth_board = request.POST.get('twelth_board')
        u.address = request.POST.get('address')
        u.district = request.POST.get('district')
        u.state = request.POST.get('state')
        u.country = request.POST.get('country')
        u.pin = request.POST.get('pin')
        u.contact = request.POST.get('contact')
        u.save()
        return HttpResponseRedirect('/student/index')
    return render(request,
            'StudentLogin/edit.html',
            {})