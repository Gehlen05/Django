# Generated by Django 4.0.6 on 2022-07-28 21:53

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_carro_montadora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='motorista',
            new_name='motoristas',
        ),
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(on_delete=models.SET(core.models.set_default_montadora), to='core.montadora'),
        ),
    ]
