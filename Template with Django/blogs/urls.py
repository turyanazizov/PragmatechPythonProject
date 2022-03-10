from django.urls import path
from blogs.views import blogs ,blog_detail

app_name='blogs'

urlpatterns = [
    path('', blogs,name='blogs'),
    path('<str:name>',blog_detail,name='blog-detail')
]