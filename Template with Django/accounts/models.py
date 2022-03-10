from django.db import models

class Accounts(models.Model):
    POSITIONS_CHOICES = (
        ('Information technologies','Information technologies'),
        ('Menegment','Menegment'),
        ('Seller','Seller'),
        ('Cashier','Cashier'),
        ('Interner','Interner'),
    )
    
    fullname=models.CharField(max_length=100,blank=False,null=False)
    department=models.CharField(max_length=100,blank=False,null=False,choices=POSITIONS_CHOICES)
    profilpicture=models.ImageField(upload_to='accountsPictures/')
    salary=models.IntegerField(blank=False,null=False)
    date=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.fullname
    
    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'

