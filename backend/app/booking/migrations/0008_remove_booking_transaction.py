# Generated by Django 3.0.7 on 2020-07-17 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20200715_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='transaction',
        ),
    ]
