from django.shortcuts import render
from .models import Project

# Create your views here.
def allProjects(request):
    projects = Project.objects
    return render(request, 'projects/allprojects.html', { 'project': projects })