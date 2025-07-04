# Generated by Django 5.2.2 on 2025-06-14 11:01

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
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_code', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('home_address', models.CharField(default='Update your account', max_length=200, null=True)),
                ('phone', models.CharField(default='Update your account', max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, max_length=12)),
                ('account_type', models.CharField(choices=[('starter', 'starter'), ('savings', 'savings'), ('standard', 'standard'), ('premium', 'premium'), ('current', 'current')], default='starter', max_length=200, null=True)),
                ('account_currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('CAD', 'CAD'), ('GBP', 'GBP')], default='EUR', max_length=200, null=True)),
                ('account_status', models.BooleanField(blank=True, default=True, null=True)),
                ('transfer_pin', models.CharField(blank=True, max_length=4, null=True)),
                ('deposit', models.FloatField(blank=True, default=0, null=True)),
                ('uncleared_balance', models.FloatField(default=0, null=True)),
                ('total_loan', models.FloatField(default=0, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foreign_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=80, null=True)),
                ('country', models.CharField(blank=True, max_length=80, null=True)),
                ('account_number', models.CharField(blank=True, max_length=80, null=True)),
                ('account_name', models.CharField(blank=True, max_length=80, null=True)),
                ('bank_code', models.CharField(blank=True, max_length=80, null=True)),
                ('routing_number', models.CharField(blank=True, max_length=80, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='herculesbankapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=12, null=True)),
                ('account_name', models.CharField(blank=True, max_length=12, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='herculesbankapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_account_number', models.CharField(blank=True, max_length=12, null=True)),
                ('destination_account_name', models.CharField(blank=True, max_length=65, null=True)),
                ('destination_account_email', models.CharField(blank=True, max_length=65, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='herculesbankapp.client')),
            ],
        ),
    ]
