# Generated by Django 4.2.1 on 2023-05-24 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_order_alter_product_price_alter_product_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]