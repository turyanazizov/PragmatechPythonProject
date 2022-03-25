from django.db import models

class Contact(models.Model):
    fname=models.CharField(max_length=100,blank=False,null=False)
    lname=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField()
    comment=models.TextField()
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fname} {self.lname}'s comment"
        
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'

