# Generated by Django 3.0.7 on 2020-07-13 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mooring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('lake', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lake.Lake')),
            ],
        ),
    ]
