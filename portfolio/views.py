from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    # Grab all objects from database that are project objects
    projects = Project.objects.all()
    # pass dictionary into template that contains projects from database
    return render(request, 'portfolio/home.html', {'projects':projects})
