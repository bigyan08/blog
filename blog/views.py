from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView, CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # here '-' sign changes the order of the posts from oldest2latest to latest2oldest
    paginate_by =5 #no. of posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by =5 #no. of posts per page
    
    def get_queryset(self):
        username =get_object_or_404(User,username=self.kwargs.get('username'))
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model= Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model =Post
    fields =['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Post
    fields =['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =Post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    success_url = '/'
       
def about(request):
   return render(request,'blog/about.html',{'title':'About'}) 


