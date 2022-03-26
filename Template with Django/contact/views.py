from django.shortcuts import render,redirect
from . models import Contact
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been received!')
            return redirect(reverse('contact:contact'))

    return render(request, 'contact/contact.html', {'form': form})

    # if request.method == 'POST':
    #     Contact.objects.create(
    #         fname=request.POST.get('fname'),
    #         lname=request.POST.get('lname'),
    #         email=request.POST.get('email'),
    #         comment=request.POST.get('comment'),
    #     )
    #     return redirect('contact:contact')
