# Generated by Django 3.2 on 2021-05-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0002_auto_20210524_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='room_no',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
