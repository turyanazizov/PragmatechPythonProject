from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    author=models.CharField(max_length=100,blank=False,null=False)
    date=models.DateTimeField(auto_now=True)


def __str__(self) :
        return self.title
    
class Meta:
    verbose_name='Blog'
    verbose_name_plural='Blogs'
