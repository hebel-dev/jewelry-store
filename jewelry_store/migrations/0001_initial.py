# Generated by Django 4.0.1 on 2022-02-15 15:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=50)),
                ('material', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('wood&gold', 'wood&gold'), ('wood&silver', 'wood&silver')], default='silver', max_length=50)),
                ('purity', models.CharField(choices=[('.999', '.999'), ('.925', '.925'), ('.875', '.875'), ('.830', '.830'), ('.800', '.800'), ('.960', '.960'), ('.750', '.750'), ('.585', '.585'), ('.500', '.500'), ('.375', '.375'), ('.333', '.333')], default='.925', max_length=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('slug', models.SlugField(max_length=255)),
                ('in_stock', models.BooleanField(default=True)),
                ('not_new', models.BooleanField(default=True)),
                ('size', models.CharField(blank=True, choices=[('5/ø14mm/US4', '5/ø14mm/US4'), ('6/ø14.3mm/US4+', '6/ø14.3mm/US4+'), ('7/ø14.6mm/', '7/ø14.6mm/'), ('8/ø15mm/US5', '8/ø15mm/US5'), ('9/ø15.3mm', '9/ø15.3mm'), ('10/ø15.6mm/US6-', '10/ø15.6mm/US6-'), ('11/ø16mm/US6', '11/ø16mm/US6'), ('12/ø16.3mm', '12/ø16.3mm'), ('13/ø16.6mm', '13/ø16.6mm'), ('14/ø17mm/US7', '14/ø17mm/US7'), ('15/ø17.3mm', '15/ø17.3mm'), ('16/ø17.6mm/US7+', '16/ø17.6mm/US7+'), ('17/ø18mm/US8', '17/ø18mm/US8'), ('18/ø18.3mm', '18/ø18.3mm'), ('19/ø18.6mm/US9', '19/ø18.6mm/US9'), ('20/ø19mm', '20/ø19mm'), ('21/ø19.3mm/US9+', '21/ø19.3mm/US9+'), ('22/ø19.6mm/US10', '22/ø19.6mm/US10'), ('23/ø20mm', '23/ø20mm'), ('24/ø20.3mm/US11-', '24/ø20.3mm/US11-'), ('25/ø20.6mm/US11', '25/ø20.6mm/US11'), ('26/ø21mm', '26/ø21mm'), ('27/ø21.3/US12', '27/ø21.3/US12'), ('28/ø21.6', '28/ø21.6'), ('29/ø22mm/US13-', '29/ø22mm/US13-'), ('30/ø22.3mm/US13', '30/ø22.3mm/US13'), ('31/ø22.6mm', '31/ø22.6mm'), ('32/ø23mm/US14', '32/ø23mm/US14'), ('33/ø23.3mm', '33/ø23.3mm'), ('34/ø23.6mm', '34/ø23.6mm')], max_length=17, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='jewelry_store.category')),
                ('colection_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='jewelry_store.collection')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created', '-updated', 'weight', 'price'),
            },
        ),
    ]
