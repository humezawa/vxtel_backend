from django.db import models


class Ligacao(models.Model):
    DDD_origem = models.IntegerField()
    DDD_destino = models.IntegerField()
    tempo = models.FloatField()
    plano_falemais = models.CharField(max_length=12)
