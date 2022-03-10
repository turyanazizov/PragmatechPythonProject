from django.shortcuts import render
from contact.models import Contact

def contact(request):
    contact=Contact.objects.all()
    context={
        'contacts':contact
    }
    return render(request,'contact/contact.html',context=context)
