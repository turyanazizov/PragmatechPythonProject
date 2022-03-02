from django.urls import path
from blogs.views import blogs
from contact.views import contact

urlpatterns = [
    path('',blogs),
    path('',contact)
]
