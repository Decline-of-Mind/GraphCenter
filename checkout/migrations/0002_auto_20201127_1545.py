# Generated by Django 3.0.1 on 2020-11-27 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='artwork',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='billingaddress', to='checkout.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='artwork',
            field=models.FileField(blank=True, null=True, upload_to='customer_images/%Y/%m/%d'),
        ),
    ]
