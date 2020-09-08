from django.db import models


class Ligacao(models.Model):
    FALEMAIS_PLANS = [
        (30, 'FaleMais 30'),
        (60, 'FaleMais 60'),
        (120, 'FaleMais 120')
    ]

    # escolhas disponiveis para os DDDs
    DDD = [
        ('011', '011'),
        ('016', '016'),
        ('017', '017'),
        ('018', '018')
    ]
    DDD_origem = models.CharField(max_length=3, choices=DDD)
    DDD_destino = models.CharField(max_length=3, choices=DDD)
    tempo = models.FloatField()
    plano_falemais = models.IntegerField(choices=FALEMAIS_PLANS)


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

class Image(models.Model):
    photo = models.ImageField(upload_to="gallery")