# Generated by Django 4.0 on 2021-12-23 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'MYNAME',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=150)),
                ('user_password', models.CharField(max_length=200)),
                ('user_contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('discription', models.CharField(default='', max_length=500)),
                ('Image', models.ImageField(upload_to='upload/products/')),
                ('product_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testing.category')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('coustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.user')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.product')),
            ],
        ),
    ]
