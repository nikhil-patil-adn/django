# Generated by Django 3.2.5 on 2021-07-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customer_society'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]