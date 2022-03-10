from django.shortcuts import render
from accounts.models import Accounts
def accounts(request):
    accounts=Accounts.objects.all()
    context={
        'accounts':accounts
    }

    return render(request,'accounts/accounts.html',context=context)
