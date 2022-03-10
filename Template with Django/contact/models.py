from django.db import models

class Contact(models.Model):
    fullname=models.CharField(max_length=100,blank=False,null=False)
    number=models.CharField(max_length=100,blank=False,null=False)
    adress=models.CharField(max_length=100,blank=False,null=False)
    date=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
