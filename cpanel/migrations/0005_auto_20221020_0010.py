# Generated by Django 3.2.16 on 2022-10-20 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0004_server_status_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_status',
            name='started_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='server_status',
            name='stoped_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='server_status',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
