from django.db import models


class CnabTransactions(models.Model):
    class Meta:
        ordering = ("id",)

    type = models.CharField(max_length=1)
    date = models.DateField(max_length=8)
    value = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.DateTimeField(max_length=6)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)
