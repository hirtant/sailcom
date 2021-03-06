# Generated by Django 3.0.7 on 2020-07-15 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20200715_0751'),
        ('event', '0003_auto_20200715_0751'),
        ('booking', '0005_auto_20200715_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='event.Event'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='transaction.Transaction'),
        ),
    ]
