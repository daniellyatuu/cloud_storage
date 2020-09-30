from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='windowshoppi_post_picture')
    date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
