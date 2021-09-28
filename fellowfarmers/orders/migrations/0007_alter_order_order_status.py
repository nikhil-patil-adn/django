# Generated by Django 3.2.5 on 2021-08-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210804_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('delivery_received', 'Delivery Received'), ('delivery_scheduled', 'Delivery Scheduled'), ('out_for_elivery', 'Out for Delivery'), ('delivered', 'Delivered'), ('cancel', 'Cancel')], max_length=200),
        ),
    ]