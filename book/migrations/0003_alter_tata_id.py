# Generated by Django 4.0.3 on 2023-07-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_tata_delete_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
