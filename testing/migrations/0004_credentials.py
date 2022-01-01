# Generated by Django 4.0 on 2021-12-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_user_user_addres'),
    ]

    operations = [
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'credentials',
            },
        ),
    ]