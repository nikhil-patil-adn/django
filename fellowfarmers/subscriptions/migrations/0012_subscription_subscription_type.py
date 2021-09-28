# Generated by Django 3.2.5 on 2021-07-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0011_postpaid_prepaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_type',
            field=models.CharField(choices=[('prepaid', 'Prepaid'), ('postpaid', 'Postpaid')], default='prepaid', max_length=200),
        ),
    ]