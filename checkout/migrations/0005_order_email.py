# Generated by Django 3.0.1 on 2020-11-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_orderlineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
