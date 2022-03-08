from unicodedata import name
from django.urls import path
from accounts.views import accounts

app_name='accounts'

urlpatterns = [
    path('', accounts,name='accounts'),
]