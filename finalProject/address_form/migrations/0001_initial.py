

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
