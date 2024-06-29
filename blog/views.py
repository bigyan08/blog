from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def home(request):
    return HttpResponse("<h1>this is a blog <h2>")

def about(request):
    return HttpResponse("this is about.")
