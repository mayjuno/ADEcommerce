from django.shortcuts import render, HttpResponse

# Create your views here.

def testProduct(request):
    return HttpResponse('Testing to Product Page.') 