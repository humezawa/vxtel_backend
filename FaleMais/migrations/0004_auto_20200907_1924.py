# Generated by Django 3.0.3 on 2020-09-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaleMais', '0003_auto_20200907_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligacao',
            name='DDD_destino',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='ligacao',
            name='DDD_origem',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='ligacao',
            name='plano_falemais',
            field=models.CharField(choices=[('30', 'FaleMais 30'), ('60', 'FaleMais 60'), ('120', 'FaleMais 120')], max_length=20),
        ),
    ]
