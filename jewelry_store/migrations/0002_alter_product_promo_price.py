# Generated by Django 4.0.1 on 2022-01-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promo_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
