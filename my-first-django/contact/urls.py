from django.urls import path
from blogs.views import contact

urlpatterns = [
    path('',contact),
]
