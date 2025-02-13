# Generated by Django 5.1 on 2024-08-31 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='currencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=60)),
                ('currency_code', models.CharField(max_length=3)),
                ('numeric_code', models.IntegerField()),
                ('currency_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='lookup_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='state_province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_province_code', models.CharField(max_length=6)),
                ('state_province_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='territories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.IntegerField()),
                ('country_name', models.CharField(max_length=60)),
                ('alfa_2', models.CharField(max_length=2)),
                ('alfa_3', models.CharField(max_length=3)),
                ('iso_3166_2', models.CharField(max_length=13)),
                ('region', models.CharField(max_length=10)),
                ('sub_region', models.CharField(max_length=35)),
                ('intermediate_region', models.CharField(max_length=20)),
                ('region_code', models.IntegerField()),
                ('sub_region_code', models.IntegerField()),
                ('intermediate_region_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='unit_of_measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom_code', models.CharField(max_length=3)),
                ('uom_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
                ('level_category', models.CharField(max_length=6)),
                ('symbol', models.CharField(max_length=30)),
                ('conversion_factor', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='lookup_values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_value', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('lookup_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fnd.lookup_type')),
            ],
        ),
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(max_length=10)),
                ('city_name', models.CharField(max_length=60)),
                ('state_province_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fnd.state_province')),
            ],
        ),
        migrations.AddField(
            model_name='state_province',
            name='country_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fnd.territories'),
        ),
        migrations.CreateModel(
            name='territory_taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory_tax_code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=60)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fnd.territories')),
            ],
        ),
    ]
