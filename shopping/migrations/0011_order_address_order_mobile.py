# Generated by Django 4.1.6 on 2023-02-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.BigIntegerField(default=None),
        ),
    ]
