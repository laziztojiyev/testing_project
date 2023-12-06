from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=255)
    stocks = models.IntegerField(default=0)
    tonnes = models.IntegerField()


class Stocks(models.Model):
    cities = models.ForeignKey('apps.Cities', on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=255)


class Fruits(models.Model):
    stocks = models.ForeignKey('apps.Stocks', on_delete=models.CASCADE, related_name='stocks')
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
