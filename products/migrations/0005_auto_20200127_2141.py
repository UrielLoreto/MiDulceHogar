# Generated by Django 3.0.2 on 2020-01-28 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200127_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product',
            new_name='product_id',
        ),
    ]
