# Generated by Django 3.0.7 on 2020-07-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='duration_weekday',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='duration_weekend',
            field=models.DurationField(blank=True, null=True),
        ),
    ]