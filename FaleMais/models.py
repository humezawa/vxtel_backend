from django.db import models


# classe de armazenamento de tarifas padrao por DDD de origem e destino
class Tarifa(models.Model):
    data = models.DateTimeField(auto_now_add=True, name='Ultima Atualização')
    DDD_origem = models.CharField(max_length=3)
    DDD_destino = models.CharField(max_length=3)
    preco_por_minuto = models.FloatField()

    # meta classe de definicao de plural
    class Meta:
        verbose_name_plural = "Tarifas"

    # define o nome no gerenciador em admin
    def __str__(self):
        return '{} -> {}'.format(self.DDD_origem, self.DDD_destino)
