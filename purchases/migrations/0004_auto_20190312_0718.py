# Generated by Django 2.1.7 on 2019-03-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_auto_20190311_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='purchase_id'),
        ),
    ]
