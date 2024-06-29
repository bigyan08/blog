from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'title':'Blog post 1',
        'content':'hello world',
        'author':'Hero1',
        'date_posted':'September 21, 2003'
    },
    {
        'title':'Blog post 2',
        'content':'hello world 2',
        'author':'Hero2',
        'date_posted':'September 22, 2003'
    },
    {
        'title':'Blog post 2',
        'content':'hello world 3',
        'author':'Hero2',
        'date_posted':'September 23, 2003'
    }

]

# Create your views here
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
   return render(request,'blog/about.html',{'title':'About'}) 
