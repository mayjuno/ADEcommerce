from math import degrees
from django.shortcuts import render
#from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    name = 'Dr Kyaw Myo Swe'
    degrees = ['B.C.Sc','ME(IT)','Ph.D(Information Technology']
    jobs = 'Software Enginner'
    context ={
        'name' : name,
        'degrees' : degrees,
        'jobs' : jobs,
    }
    return render(request,'index.html',context)
    #return HttpResponse("Hello Django!")