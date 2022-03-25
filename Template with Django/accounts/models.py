from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=True, unique=True)
    bio = models.TextField(blank=True, null=True, help_text='Give some information about yourself')
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username','image']
    
    @property
    def user_image(self):
        if self.image:
            return self.image
        return 'https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png'


