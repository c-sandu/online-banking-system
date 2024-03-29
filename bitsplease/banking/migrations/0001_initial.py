# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('user_type', models.CharField(choices=[('CST', 'Customer'), ('VND', 'Vendor'), ('BNK', 'Banker'), ('ADM', 'ADMIN')], default='CST', max_length=3)),
                ('auth_seed', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', models.CharField(max_length=34, unique=True)),
                ('acc_type', models.CharField(choices=[('CUR', 'Current'), ('SVG', 'Savings')], default='CUR', max_length=3)),
                ('balance', models.DecimalField(decimal_places=6, max_digits=15)),
                ('currency', models.CharField(max_length=3)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
                ('date_last_touch', models.DateTimeField(verbose_name='date last touch')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.CharField(max_length=10, unique=True)),
                ('amount', models.DecimalField(decimal_places=6, max_digits=15)),
                ('currency', models.CharField(max_length=3)),
                ('date', models.DateTimeField(verbose_name='date transaction')),
                ('message', models.CharField(max_length=255)),
                ('dst_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_dst_acc', to='banking.Account')),
                ('src_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_src_acc', to='banking.Account')),
            ],
        ),
    ]
