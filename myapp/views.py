from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.forms import PostsForm
from django.views.generic import ListView,CreateView,UpdateView
from myapp.models import Banner
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.

class CreatePostView(CreateView):
    template_name: str="index.html"
    model=Banner
    form_class=PostsForm
    success_url=reverse_lazy("index")
    context_object_name="post"
    def get_queryset(self):
        return Banner.objects.all()
class PostList(ListView):
    model=Banner
    template_name: str="post-list.html"
    context_object_name="post"
    def get_queryset(self):
        return Banner.objects.all()    
class UpdatePostView(UpdateView):
    model=Banner
    form_class=PostsForm
    template_name: str="update.html"
    success_url=reverse_lazy("post-list") 
    pk_url_kwarg:str="id"
    def from_valid(self,form):
        return super().form_valid(form)   
def post_delete(request,*args,**kwargs):
    post_id=kwargs.get("id")
    Banner.objects.filter(id=post_id).delete()
    # messages.success(request,"Post Deleted Successfully")
    return redirect("post-list")

