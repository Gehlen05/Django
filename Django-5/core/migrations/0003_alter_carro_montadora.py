# Generated by Django 4.0.6 on 2022-07-28 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carro_motorista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.montadora'),
        ),
    ]
