# Generated by Django 4.2.1 on 2023-05-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
