from django.shortcuts import render
from .models import School
# Create your views here.
def school(request):
    details = School.objects
    return render(request, 'schools/schoolinfo.html', {'info': details})