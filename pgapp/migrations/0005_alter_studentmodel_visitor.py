# Generated by Django 3.2 on 2021-05-25 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0004_rename_avail_till_studentmodel_availed_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='visitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pgapp.visitormodel'),
        ),
    ]