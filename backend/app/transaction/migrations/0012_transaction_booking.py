# Generated by Django 3.0.7 on 2020-07-27 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_remove_booking_transaction'),
        ('transaction', '0011_auto_20200727_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='booking',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='booking.Booking'),
        ),
    ]
