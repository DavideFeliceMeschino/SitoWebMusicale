# Generated by Django 4.2.6 on 2023-12-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0031_commenti_data_inserimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commenti',
            name='data_inserimento',
        ),
    ]