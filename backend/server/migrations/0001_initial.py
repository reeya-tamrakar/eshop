# Generated by Django 2.2.5 on 2021-02-25 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('img1', models.ImageField(upload_to='shop/products')),
                ('in_stock', models.BooleanField(default=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.ProductCategory')),
            ],
        ),
    ]
