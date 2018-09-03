from django.shortcuts import render
from django.db.models import Count, Q
from .models import Passenger

# Create your views here.

def ticket_class_view(request):
