# Generated by Django 2.1.7 on 2019-03-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0004_auto_20190312_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
