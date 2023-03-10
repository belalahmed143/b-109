from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='ProfileImage', default='ProfileImage/no_profile.png' )
    phone  = models.CharField(max_length = 14, blank=True,null=True)
    dobd  = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return self.user.username
    
    
    

