# Generated by Django 4.1.1 on 2023-02-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "administrativelevels",
            "0013_rename_unit_geographic_cvd_geographical_unit_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="geographicalunit",
            name="attributed_number_in_canton",
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
