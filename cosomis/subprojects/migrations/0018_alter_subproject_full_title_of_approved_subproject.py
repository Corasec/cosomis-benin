# Generated by Django 4.1.1 on 2023-03-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subprojects', '0017_subproject_direct_beneficiaries_men_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='full_title_of_approved_subproject',
            field=models.TextField(),
        ),
    ]
