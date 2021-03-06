# Generated by Django 3.0.7 on 2020-07-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0002_auto_20200714_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='price_full_day',
            new_name='price_fullday_weekday',
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='price_weekday',
            new_name='price_fullday_weekend',
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='price_weekend',
            new_name='price_hour_weekday',
        ),
        migrations.AddField(
            model_name='boat',
            name='price_hour_weekend',
            field=models.DecimalField(decimal_places=10, default=20, max_digits=19),
            preserve_default=False,
        ),
    ]
