from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
   blogs = Blog.objects.order_by('-date')
   return render(request,'blog/all_blogs.html',{
      'blogs':blogs,
   })

def blog_detail(request,id):
   blog = get_object_or_404(Blog,id=id)
   return render(request,'blog/blog_detail.html',{
      'blog':blog,
   })