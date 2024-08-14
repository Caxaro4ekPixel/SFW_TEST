# Generated by Django 5.1 on 2024-08-14 15:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contract_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contract',
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.manufacturer')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='CreditApplication',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='credit_application', to='core.contract')),
                ('products', models.ManyToManyField(related_name='credit_applications', to='core.product')),
            ],
            options={
                'verbose_name': 'CreditApplication',
                'verbose_name_plural': 'CreditApplications',
                'db_table': 'credit_application',
            },
        ),
    ]
