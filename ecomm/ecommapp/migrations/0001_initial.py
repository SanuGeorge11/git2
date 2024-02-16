# Generated by Django 5.0.1 on 2024-02-07 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('price', models.PositiveBigIntegerField()),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('description', models.CharField(max_length=100)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommapp.category')),
            ],
        ),
    ]