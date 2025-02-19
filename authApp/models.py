from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilePic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')
    
    
    def __str__(self) -> str:
	    return self.user.username