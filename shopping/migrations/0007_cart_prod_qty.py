# Generated by Django 4.1.6 on 2023-02-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='prod_qty',
            field=models.IntegerField(default=None),
        ),
    ]
