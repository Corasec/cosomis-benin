# Generated by Django 4.1.1 on 2023-02-24 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrativelevels", "0010_rename_unitgeographic_geographicalunit"),
    ]

    operations = [
        migrations.AddField(
            model_name="cvd",
            name="headquarters_village",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="headquarters_village_of_the_cvd",
                to="administrativelevels.administrativelevel",
            ),
        ),
    ]
