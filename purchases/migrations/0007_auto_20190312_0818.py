# Generated by Django 2.1.7 on 2019-03-12 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0006_purchase_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='email',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
