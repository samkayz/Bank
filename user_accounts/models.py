from django.db import models


class Customer (models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    acct_no = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

