# Generated by Django 3.0.7 on 2020-07-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20200717_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='max_participants',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
