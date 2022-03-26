from wsgiref.validate import validator
from django import forms
from django.forms import ModelForm, ValidationError
from contact.models import Contact
from django import forms

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'fname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'first name...',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email...'
            }),

            'lname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'last name...'
            }),

            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'message here...'
            }),
        }    

    def clean_fname(self):
        fname = self.cleaned_data['fname']
        if not fname.istitle():
            raise ValidationError('This is not valid first name')
        return fname

    def clean_lname(self):
        lname = self.cleaned_data['lname']
        if not lname.istitle():
            raise ValidationError('This is not valid last name')
        return lname
    
    def clean_comment(self):
        comment = self.cleaned_data['comment']
        if not len(comment)>10:
            raise ValidationError('This messsage is short')
        return comment

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('gmail.com'):
            raise ValidationError('Only gmail.com emails are accepted')
        return email
    
