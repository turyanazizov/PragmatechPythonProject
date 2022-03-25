from django.shortcuts import render,redirect
from . models import Contact

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            comment=request.POST.get('comment'),
        )
        return redirect('contact:contact')
    return render(request,"contact/contact.html")
