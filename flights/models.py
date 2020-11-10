from djongo import models

# Create your models here.


class Flight(models.Model):
    departure = models.CharField(max_length=80)
    arrival = models.CharField(max_length=80)
    price = models.IntegerField()
    book_link = models.CharField(max_length=120)