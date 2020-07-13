# Generated by Django 3.0.7 on 2020-07-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200713_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address_appendix',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='entry_fee_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='licence_ok',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='zip',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
