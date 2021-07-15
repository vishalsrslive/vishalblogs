from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blogs.html')
    # return HttpResponse("This is home page")
def blogs(request):
    return HttpResponse("This is blogs page")
def static(request):
    return HttpResponse("This is blogs page")