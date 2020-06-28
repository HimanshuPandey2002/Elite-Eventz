from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'about/about.html')

def FAQs(request):
    return render(request,'about/FAQ.html')

