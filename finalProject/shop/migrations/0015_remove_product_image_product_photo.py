# Generated by Django 4.0.6 on 2022-08-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_order_delete_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
