# Generated by Django 3.0.7 on 2020-07-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
