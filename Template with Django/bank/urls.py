from django.urls import path
from .views import bank
app_name='bank'

urlpatterns = [    
    path('', bank,name='bank'),
]