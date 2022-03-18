from django.db import models

class Bank(models.Model): 
    name=models.CharField(max_length=100,blank=False,null=False)
    owner=models.CharField(max_length=100,blank=False,null=False)
    # Relations
    def __str__(self):
        return self.name

class Filial(models.Model):
    adress=models.CharField(max_length=100,blank=False,null=False)
    customer=models.IntegerField(blank=False,null=False)
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE,related_name="b")
    
    def __str__(self):
        return self.adress




