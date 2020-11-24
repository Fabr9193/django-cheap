from djongo import models

# Create your models here.
# TODO mettre a  jour les datas pour refleter toutes les données qu'on peut récuperer/utiliser


class Flight(models.Model):
    departure = models.CharField(max_length=80)
    arrival = models.CharField(max_length=80)
    price = models.IntegerField()
    book_link = models.CharField(max_length=120)