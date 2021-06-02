from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz



class Loc(models.Model):
    Location =  models.CharField(max_length=255)
    def __str__(self):
        return self.Location



class source(models.Model):
    source =  models.CharField(max_length=255)
    def __str__(self):
        return self.source


class status(models.Model):
    status_cos =  models.CharField(max_length=255)
    def __str__(self):
        return self.status_cos

class Marketing_update(models.Model):
    auto_date =  models.DateTimeField(default=timezone.now)
    customer_Name = models.CharField(max_length=255)
    customer_Number =  models.CharField(max_length=255)
    customer_Location =  models.ForeignKey(Loc, on_delete=models.CASCADE)
    customer_Source =  models.ForeignKey(source, on_delete=models.CASCADE)
    confirmation_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    status   = models.ForeignKey(status,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_Name


    def get_absolute_url(self):
        return reverse('homepage')

