import email
from email import message
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Rickshaw(models.Model):
    destination=models.CharField(max_length=200)
    fare=models.IntegerField()
    name=models.CharField(max_length=100)
    phone=models.IntegerField()



class Bus(models.Model):
    Route=models.CharField(max_length=200)
    fare=models.IntegerField()
    time=models.CharField(max_length=20)
    Book_Now=models.CharField(max_length=100)
   



class Van(models.Model):
    destination=models.CharField(max_length=200)
    fare=models.IntegerField()
    time=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=400)
