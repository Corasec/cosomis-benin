# Generated by Django 4.1.1 on 2022-11-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativelevels', '0007_delete_village'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativelevel',
            name='no_sql_db_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
