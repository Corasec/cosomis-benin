# Generated by Django 4.1.1 on 2022-09-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subprojects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproject',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subproject',
            name='short_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
