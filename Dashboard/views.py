from django.shortcuts import render
from .models import *

def show_dashboard(request):
    Categories=Category.objects.all()
    context={'Data':'Dashboard is working!!','Categories':Categories}
    return render(request,'dashboard.html',context)
