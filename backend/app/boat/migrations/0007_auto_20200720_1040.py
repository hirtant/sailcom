# Generated by Django 3.0.7 on 2020-07-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boat_category', '0001_initial'),
        ('boat', '0006_boat_registration_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boat',
            name='brand',
        ),
        migrations.AddField(
            model_name='boat',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boats', to='boat_category.BoatCategory'),
        ),
    ]
