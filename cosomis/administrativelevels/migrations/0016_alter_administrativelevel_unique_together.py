# Generated by Django 4.1.1 on 2023-02-25 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativelevels', '0015_cvd_created_date_cvd_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='administrativelevel',
            unique_together={('name', 'parent', 'type')},
        ),
    ]
