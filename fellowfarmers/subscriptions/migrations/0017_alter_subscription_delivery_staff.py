# Generated by Django 3.2.5 on 2021-09-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_subscription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='delivery_staff',
            field=models.CharField(blank=True, choices=[('raj', 'raj'), ('ramesh', 'ramesh')], max_length=200, null=True),
        ),
    ]