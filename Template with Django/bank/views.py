from django.shortcuts import render
from . models import Bank,Filial
def bank(request):
    bank=Bank.objects.all().first()
    filials=Filial.objects.all()
    context={
        'bank':bank,
        'filials':filials,
    }
    return render(request,'bank/bank.html',context=context)

