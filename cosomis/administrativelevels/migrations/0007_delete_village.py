# Generated by Django 4.1.1 on 2022-10-10 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativelevels', '0006_remove_administrativelevel_village_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Village',
        ),
    ]
