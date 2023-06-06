# Generated by Django 4.1.1 on 2023-06-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrativelevels", "0017_cvd_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="administrativelevel",
            name="cvd",
        ),
        migrations.RemoveField(
            model_name="administrativelevel",
            name="frontalier",
        ),
        migrations.RemoveField(
            model_name="administrativelevel",
            name="geographical_unit",
        ),
        migrations.RemoveField(
            model_name="administrativelevel",
            name="rural",
        ),
        migrations.AddField(
            model_name="administrativelevel",
            name="headquarter",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="headquarter_of",
                to="administrativelevels.administrativelevel",
                verbose_name="Chef-lieu/Préfecture",
            ),
        ),
        migrations.AlterField(
            model_name="administrativelevel",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="administrativelevel",
            name="name",
            field=models.CharField(max_length=128, verbose_name="Nom"),
        ),
        migrations.AlterField(
            model_name="administrativelevel",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="adm_children",
                to="administrativelevels.administrativelevel",
                verbose_name="Niveau administratif supérieur",
            ),
        ),
        migrations.AlterField(
            model_name="administrativelevel",
            name="type",
            field=models.CharField(
                choices=[
                    ("département", "Département"),
                    ("commune", "Commune"),
                    ("arrondissement", "Arrondissement"),
                    ("village", "Village"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="administrativelevel",
            name="updated_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]