# Generated by Django 3.0.4 on 2020-03-14 21:10

from django.db import migrations, models
import streamfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pagine', '0003_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='intro',
            field=models.CharField(default='Un altro articolo di approfondimento!', max_length=100, verbose_name='Introduzione'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='carousel',
            field=streamfield.fields.StreamField(blank=True, default='[]', help_text='Una sola galleria, per favore, larghezza minima immagini 2048px', null=True, verbose_name='Galleria orizzontale'),
        ),
    ]
