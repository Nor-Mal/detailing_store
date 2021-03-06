# Generated by Django 3.1.7 on 2021-07-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=400)),
                ('product_type', models.CharField(max_length=250)),
                ('product_brand', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
