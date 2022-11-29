from django.db import models
from houses.models import House

class Order(models.Model):
    house = models.ForeignKey(House, verbose_name='house', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=50)
    phone = models.CharField('phone', max_length=50)
    date = models.DateTimeField('date', auto_now_add=True)