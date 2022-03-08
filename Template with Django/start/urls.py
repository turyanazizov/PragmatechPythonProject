from django.urls import path
from start.views import start

app_name='start'

urlpatterns = [
    path('', start,name='start'),
]