from django.shortcuts import render

def blogs(request):
    blogs=[
        {
            'Blog 1':{
             'author':'Turyan',
             'title':'Django',
             'date':'12.02.2022'   
            },
            
            'Blog 2':{
             'author':'Ali',
             'title':'Flask',
             'date':'23.12.2021'   
            },
        }
    ]
    blogs=blogs[0]
    return render(request,'blogs/blogs.html',{'blogs':blogs})

def blog_detail(request,name):
    blogs=[
        {
            'Blog 1':{
             'author':'Turyan',
             'title':'Django',
             'date':'12.02.2022'   
            },
            
            'Blog 2':{
             'author':'Ali',
             'title':'Flask',
             'date':'23.12.2021'   
            },
        }
    ]
    blog=blogs[0][name]
    return render(request,'blogs/blog_detail.html',{'blog':blog})



