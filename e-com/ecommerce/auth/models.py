from django.db import models

class Auth(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    
