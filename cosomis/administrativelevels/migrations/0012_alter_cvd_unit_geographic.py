# Generated by Django 4.1.1 on 2023-02-24 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativelevels', '0011_cvd_headquarters_village'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvd',
            name='unit_geographic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administrativelevels.geographicalunit'),
            preserve_default=False,
        ),
    ]
