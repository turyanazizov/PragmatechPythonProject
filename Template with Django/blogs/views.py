from django.shortcuts import render
from blogs.models import Blog

def blogs(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request,'blogs/blogs.html',context=context)

def blog_detail(request,name):
    blogs=Blog.objects.all()
    blog=blogs.filter(title=name).first()
    context={
        'blog':blog
    }
    return render(request,'blogs/blog_detail.html',context=context)
