# Generated by Django 4.0.1 on 2022-04-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0007_alter_product_colection_name_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]