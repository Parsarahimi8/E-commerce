# Generated by Django 5.0.7 on 2024-07-21 12:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)])),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
