# Generated by Django 4.0.3 on 2023-07-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('trade_code', models.CharField(max_length=100)),
                ('high', models.CharField(max_length=100)),
                ('low', models.CharField(max_length=100)),
                ('open', models.CharField(max_length=100)),
                ('close', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]
