# Generated by Django 3.0.3 on 2020-09-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaleMais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ultima Atualização', models.DateTimeField(auto_now_add=True)),
                ('origem', models.CharField(max_length=3)),
                ('destino', models.CharField(max_length=3)),
                ('preco_por_minuto', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Tarifas',
            },
        ),
        migrations.RenameField(
            model_name='ligacao',
            old_name='ddd_destino',
            new_name='DDD_destino',
        ),
        migrations.RenameField(
            model_name='ligacao',
            old_name='ddd_origem',
            new_name='DDD_origem',
        ),
    ]
