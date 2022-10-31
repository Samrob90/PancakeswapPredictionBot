# Generated by Django 3.2.16 on 2022-10-31 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0009_alter_pancakeswappredicition_epoch'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_hash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.IntegerField(default=None)),
                ('transaction_hash', models.TextField(blank=True, default=None, null=True)),
                ('wallet_number', models.IntegerField(default=None)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]