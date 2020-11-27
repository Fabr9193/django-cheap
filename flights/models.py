from djongo import models
from django.contrib.auth import get_user_model

# Create your models here.
# TODO mettre a  jour les datas pour refleter toutes les données qu'on peut récuperer/utiliser


class Flight(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    departure = models.CharField(max_length=80)
    arrival = models.CharField(max_length=80)
    price = models.IntegerField()
    duration = models.IntegerField()
    airline = models.CharField(max_length=80)
    book_link = models.CharField(max_length=120)