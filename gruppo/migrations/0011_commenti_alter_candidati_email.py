# Generated by Django 4.2.6 on 2023-12-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0010_alter_artisti_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commenti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('commento', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='candidati',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
