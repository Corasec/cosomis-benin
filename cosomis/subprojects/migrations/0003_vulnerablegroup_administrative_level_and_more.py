# Generated by Django 4.1.1 on 2022-09-29 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrativelevels", "0003_alter_administrativelevel_latitude_and_more"),
        ("subprojects", "0002_subproject_description_subproject_short_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="vulnerablegroup",
            name="administrative_level",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrativelevels.administrativelevel",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="subproject",
            name="priorities",
            field=models.ManyToManyField(
                blank=True, null=True, to="subprojects.communitypriority"
            ),
        ),
    ]
