# Generated by Django 3.2.20 on 2023-10-05 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_proj', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]