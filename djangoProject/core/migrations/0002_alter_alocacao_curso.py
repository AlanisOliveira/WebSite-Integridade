# Generated by Django 4.2.2 on 2023-07-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alocacao',
            name='curso',
            field=models.CharField(max_length=100),
        ),
    ]
