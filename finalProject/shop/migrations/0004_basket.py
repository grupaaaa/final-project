# Generated by Django 4.0.6 on 2022-08-06 19:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address_form', '0001_initial'),
        ('shop', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_form.shippingaddress')),
            ],
        ),
    ]
