from django.db import models

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    subject= models.CharField(max_length=100)
 
        