# Generated by Django 4.2.6 on 2023-12-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0013_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenti',
            name='commento',
            field=models.CharField(max_length=250),
        ),
    ]
