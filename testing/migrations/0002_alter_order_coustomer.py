# Generated by Django 4.0 on 2021-12-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coustomer',
            field=models.CharField(max_length=100),
        ),
    ]
