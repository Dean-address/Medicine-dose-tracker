from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dosage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dosages')
    medicine_name = models.CharField(max_length=100,blank=False)
    quantity = models.IntegerField(blank=False)
    units = models.CharField(max_length=50, blank=False)
    frequency = models.CharField(max_length=50, blank=False)
    
    def __str__(self) -> str:
        return self.medicine_name