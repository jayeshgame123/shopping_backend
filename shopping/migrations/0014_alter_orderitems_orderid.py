# Generated by Django 4.1.6 on 2023-02-22 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_remove_cart_prodid_remove_cart_prod_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shopping.order'),
        ),
    ]
