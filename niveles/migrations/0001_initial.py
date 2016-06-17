# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nivelesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('juego', models.CharField(max_length=50)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.actividadesModel')),
            ],
        ),
    ]