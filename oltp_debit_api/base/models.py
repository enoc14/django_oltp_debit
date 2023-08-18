from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    balance = models.FloatField()
    open_date = models.DateField()

    def __str__(self):
        return self.user.name


class Card(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.name
