# Generated by Django 3.0.1 on 2020-10-26 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
    ]
