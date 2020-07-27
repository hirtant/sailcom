# Generated by Django 3.0.7 on 2020-07-27 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0013_remove_transaction_booking'),
        ('booking', '0014_remove_booking_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='transaction.Transaction'),
        ),
    ]
